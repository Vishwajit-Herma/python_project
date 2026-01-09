class APIError(Exception):
    """Raised when API request fails"""
    pass


class DataProcessingError(Exception):
    """Raised when data processing fails"""
    pass


class StorageError(Exception):
    """Raised when file storage fails"""
    pass
