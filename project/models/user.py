from project.models.base_model import BaseModel
from project import db, bcrypt


class User(BaseModel):
    '''
    Represents an user, with email, password, fullname and photo
    '''
    __tablename__ = 'users'

    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password, fullname, photo):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
        self.fullname = fullname
        self.photo = photo

    def update(self, email = None, password = None, fullname = None, photo = None, **kwargs):
        if email:
            self.email = email
        if password:
            self.password = bcrypt.generate_password_hash(password).decode("utf-8")
        if fullname:
            self.fullname = fullname
        if photo:
            self.photo = photo
        super().update(**kwargs)

    def is_correct_password(self, plaintext_password: str) -> bool:
        return bcrypt.check_password_hash(self.password, plaintext_password)