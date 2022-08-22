class User:
    '''
    Represents an user, with email, password, fullname and photo
    '''

    def __init__(self, email, password, fullname, photo):
        self.email = email
        self.password = password
        self.fullname = fullname
        self.photo = photo