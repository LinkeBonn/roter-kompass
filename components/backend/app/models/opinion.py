from app.extensions import db

class Opinion(db.Model):
    __tablename__ = "opinion"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=True)
    text = db.Column(db.Text, nullable=False)

    action_id = db.Column(db.String(6), db.ForeignKey("action.id"), nullable=False)
    action = db.relationship("Action", backref=db.backref("opinion", lazy=True))
