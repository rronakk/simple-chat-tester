class ImproperlyConfigured(Exception):
    """Exceptions for unset environment variables"""
    def __init__(self, value):
        """Summary

        Args:
            value (TYPE): Description
        """
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)
