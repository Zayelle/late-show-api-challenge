from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest_bp', __name__)

# GET /guests — List all guests (❌ No auth required)
@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    response = [
        {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        }
        for guest in guests
    ]
    return jsonify(response), 200
