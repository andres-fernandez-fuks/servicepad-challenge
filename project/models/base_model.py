from datetime import datetime
from project import db

class BaseModel(db.Model):
    """
    Base model class.
    """
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now())

    def update(self):
        # Only updated_at should be able to be updated
        self.updated_at = datetime.now()
