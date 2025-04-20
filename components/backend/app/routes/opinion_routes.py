from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.opinion import Opinion
from app.models.action import Action
from app.schemas.opinion_schema import OpinionSchema
from app.schemas.action_schema import ActionSchema, ActionDetailSchema

opinion_bp = Blueprint("opinion", __name__)
opinion_schema = OpinionSchema()
action_schema = ActionDetailSchema()

@opinion_bp.route("/", methods=["POST"])
def create_opinion():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "Keine Daten gesendet"}), 400

    errors = opinion_schema.validate(json_data)
    if errors:
        return jsonify(errors), 400

    action = Action.query.filter_by(id=json_data["action_id"]).first()
    if not action:
        return jsonify({"error": "Action mit dieser ID existiert nicht"}), 404

    opinion = Opinion(
        author=json_data.get("author"),
        text=json_data["text"],
        action_id=json_data["action_id"]
    )
    db.session.add(opinion)
    db.session.commit()

    return jsonify(opinion_schema.dump(opinion)), 201

@opinion_bp.route("/action/<action_id>", methods=["GET"])
def get_opinion_by_action(action_id):
    action = Action.query.filter_by(id=action_id).first()
    if not action:
        return jsonify({"error": "Action nicht gefunden"}), 404

    return jsonify(action_schema.dump(action)), 200