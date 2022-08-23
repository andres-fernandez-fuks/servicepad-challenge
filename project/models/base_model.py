from datetime import datetime
from project import db

class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now())

    def update(self, updated_at=None):
        # Only updated_at should be able to be updated
        if updated_at:
            self.updated_at = updated_at
