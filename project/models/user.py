from project.models.base_model import BaseModel

class User(BaseModel):
    '''
    Represents an user, with email, password, fullname and photo
    '''

    def __init__(self, email, password, fullname, photo):
        self.email = email
        self.password = password
        self.fullname = fullname
        self.photo = photo

    def update(self, email = None, password = None, fullname = None, photo = None, **kwargs):
        if email:
            self.email = email
        if password:
            self.password = password
        if fullname:
            self.fullname = fullname
        if photo:
            self.photo = photo
        super().update(**kwargs)