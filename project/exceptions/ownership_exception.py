class OwnershipException(Exception):
    """
    Exception raised when a user does not own a resource.
    It is not intended to give a lot of information about the cause of the error.
    """

    def __str__(self):
        return "There was a problem validating the ownership of the publication."
