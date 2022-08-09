"""Shared memory object to pass data between extractors and/or transformers"""


class BaseSharedMemory:
    """
    Shared memory object to pass data between extractors and/or transformers.

    This is used to store some "general / cached" data.
    It should be avoided if possible, however it might make the writer life much easier
    """

    def __init__(self) -> None:
        """
        Init shared object.

        More init can be added
        """
        pass
