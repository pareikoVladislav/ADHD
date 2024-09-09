class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    @classmethod
    def bad_request(cls, message):
        return cls(400, message)

    @classmethod
    def unauthorized(cls, message):
        return cls(401, message)

    @classmethod
    def forbidden(cls, message):
        return cls(403, message)

    @classmethod
    def not_found(cls, message):
        return cls(404, message)

    @classmethod
    def server_error(cls, message):
        return cls(500, message)
