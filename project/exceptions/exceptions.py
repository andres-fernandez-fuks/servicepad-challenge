class OwnershipException(Exception):
    """
    Exception raised when a user does not own a resource.
    It is not intended to give a lot of information about the cause of the error.
    """

    def __str__(self):
        return "There was a problem validating the ownership of the publication."


class AuthenticationException(Exception):
    pass

    def __str__(self):
        return "There was a problem validating the authentication of the user."


class ObjectNotFoundException(Exception):
    def __init__(self, object_type, object_id):
        self.object_type = object_type
        self.object_id = object_id

    def __str__(self):
        return f"The {self.object_type} with id {self.object_id} was not found."