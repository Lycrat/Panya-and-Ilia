class NoIceException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.message = message
        self.errors = errors
        

    def __str__(self):
        return f"{self.message} (Error code: {self.errors})"