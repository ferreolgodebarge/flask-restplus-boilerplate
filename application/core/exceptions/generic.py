class GenericException(Exception):
    """[Exception Wrapper]

    Arguments:
        Exception {[Exception]} -- [Exception class]

    Returns:
        [GenericException] -- [Exception with specific status code]
    """
    status_code = 400

    def __init__(self, message):
        """[Initializer]

        Arguments:
            message {[String]} -- [Message to be sent when exception raises]
        """
        self.message = message

    def to_dict(self):
        return {
            "status": "FAILED",
            "message": self.message,
        }


class ResourceNotFound(GenericException):
    status_code = 404


class BackendIssue(GenericException):
    status_code = 503


class ConflictError(GenericException):
    status_code = 409


class InvalidParameter(GenericException):
    status_code = 400
