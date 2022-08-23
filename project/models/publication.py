from datetime import datetime
from project.models.base_model import BaseModel
from project import db

class Publication(BaseModel):
    """
    Represents an user's publication, with title, description, priority, status, time since creation, user, created_at, updated_at
    """

    __tablename__ = "publications"

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("publications", lazy=True))

    def __init__(
        self,
        title,
        description,
        priority,
        status,
        user_id,
    ):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.time_since_creation = datetime.now() - self.created_at if self.created_at else None
        self.user_id = user_id

    def update(
        self, title=None, description=None, priority=None, status=None, **kwargs
    ):
        if title:
            self.title = title
        if description:
            self.description = description
        if priority:
            self.priority = priority
        if status:
            self.status = status
        super().update(**kwargs)
