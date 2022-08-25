class AuthenticationException(Exception):
    pass

    def __str__(self):
        return "There was a problem validating the authentication of the user."