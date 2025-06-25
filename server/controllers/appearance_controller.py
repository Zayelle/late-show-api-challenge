from flask import Blueprint, request, jsonify
from server.models import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from flask_jwt_extended import jwt_required, get_jwt_identity

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    current_user = get_jwt_identity()  # Not used in logic but good for logging/auditing

    data = request.get_json()

    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    rating = data.get('rating')

    # Validate presence of required fields
    if guest_id is None or episode_id is None or rating is None:
        return jsonify({"error": "guest_id, episode_id, and rating are required."}), 400

    # Validate rating range
    if not isinstance(rating, int) or not (1 <= rating <= 5):
        return jsonify({"error": "Rating must be an integer between 1 and 5."}), 400

    # Validate foreign key existence
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)

    if not guest:
        return jsonify({"error": f"Guest with ID {guest_id} does not exist."}), 404
    if not episode:
        return jsonify({"error": f"Episode with ID {episode_id} does not exist."}), 404

    try:
        appearance = Appearance(
            guest_id=guest_id,
            episode_id=episode_id,
            rating=rating
        )
        db.session.add(appearance)
        db.session.commit()

        return jsonify({
            "id": appearance.id,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "rating": appearance.rating
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

