from marshmallow import Schema, fields, validate

class OpinionSchema(Schema):
    id = fields.Int(dump_only=True)
    author = fields.String(required=False, allow_none=True, validate=validate.Length(max=100))
    text = fields.String(required=True, validate=validate.Length(min=1))
    action_id = fields.String(required=True, validate=validate.Length(equal=6))
