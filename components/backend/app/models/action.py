import random
import string
from app.extensions import db

def generate_unique_id():
    while True:
        new_id = ''.join(random.choices(string.digits, k=6))
        exists = db.session.query(
            db.session.query(Action).filter_by(id=new_id).exists()
        ).scalar()
        if not exists:
            return new_id

class Action(db.Model):
    __tablename__ = "action"

    id = db.Column(db.String(6), primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    group_actor = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    opinions = db.relationship("Opinion", backref="parent_action", lazy=True)

    def __init__(self, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = generate_unique_id()
        super().__init__(**kwargs)
