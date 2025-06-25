from flask import Blueprint, jsonify
from server.models import db
from server.models.episode import Episode
from flask_jwt_extended import jwt_required, get_jwt_identity

episode_bp = Blueprint('episode_bp', __name__)

# GET /episodes — List all episodes (❌ No auth required)
@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    response = [
        {
            "id": ep.id,
            "date": ep.date.isoformat(),
            "number": ep.number
        }
        for ep in episodes
    ]
    return jsonify(response), 200

# GET /episodes/<int:id> — Get single episode + its appearances (❌ No auth required)
@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    response = {
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": [
            {
                "id": ap.id,
                "guest_id": ap.guest_id,
                "rating": ap.rating
            }
            for ap in episode.appearances
        ]
    }
    return jsonify(response), 200

# DELETE /episodes/<int:id> — Delete episode + its appearances (✅ Auth required)
@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    current_user = get_jwt_identity()  # Optional: for logging or future access control

    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": f"Episode with ID {id} not found."}), 404

    try:
        db.session.delete(episode)
        db.session.commit()
        return jsonify({"message": f"Episode {id} and its appearances were deleted."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

