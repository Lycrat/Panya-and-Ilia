class NoIceException(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.message = message
        self.error = error
        

    def __str__(self):
        return f"{self.message} (Error code: {self.error})"