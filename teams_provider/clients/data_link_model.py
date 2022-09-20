from typing import NamedTuple


class DataLink(NamedTuple):
    """
    Link returned from Microsoft APIs to additional potential requests.
    """
    url: str
    has_new_data: bool
