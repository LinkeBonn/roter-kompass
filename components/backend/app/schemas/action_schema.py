from marshmallow import Schema, fields, validate
from app.schemas.opinion_schema import OpinionSchema

class ActionSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    group_actor = fields.String(required=True, validate=validate.Length(min=1, max=100))
    description = fields.String(allow_none=True)

class ActionDetailSchema(ActionSchema):
    opinions = fields.Nested(OpinionSchema, many=True)