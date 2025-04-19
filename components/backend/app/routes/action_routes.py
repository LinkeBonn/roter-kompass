from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.action import Action
from app.schemas.action_schema import ActionSchema

action_bp = Blueprint("action", __name__)
action_schema = ActionSchema()

@action_bp.route("/", methods=["POST"])
def create_action():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "Keine Daten gesendet"}), 400

    errors = action_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    action = Action(
        name=json_data["name"],
        group_actor=json_data["group_actor"],
        description=json_data.get("description")
    )
    db.session.add(action)
    db.session.commit()

    return jsonify(action_schema.dump(action)), 201

@action_bp.route("/<action_id>", methods=["GET"])
def get_action_with_opinions(action_id):
    action = Action.query.filter_by(id=action_id).first()
    if not action:
        return jsonify({"error": "Action not found"}), 404

    return jsonify(action_schema.dump(action)), 200
