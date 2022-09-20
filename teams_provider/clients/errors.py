class ResourceNotFoundError(Exception):
    """
    Raised when API returns 404 error.
    """


class AccessDeniedError(Exception):
    """
    Raised when API return 403 error.
    """


class InvalidAuthenticationToken(Exception):
    """
    Raised when API return 401 error.

    """


class RoleNotMappedError(Exception):
    """
    Raised when a role is not mapped in constants.

    """


class GatewayTimeoutException(Exception):
    """
    Raised when we have gateway timed out exception
    """
    pass


class SyncErrorException(Exception):
    """
    Raised when we have to re sync a resource
    """


class UnsupportedRequestError(Exception):
    """
    Raised when we have an unsupported request to the Graph APi.
    For example a delta link older than 30 days!! OR Sorting not supported for query
    https://developer.microsoft.com/en-us/identity/blogs/build-advanced-queries-with-count-filter-search-and-orderby/
    """
