from typing import Iterable

from base_provider import BaseExtractor


class FilesExtactor(BaseExtractor):
    def extact_raw(self) -> Iterable[dict]:
        return [
            {
                "id": "A",
                "name": "file-1",
            },
            {
                "id": "B",
                "name": "file-2",
            },
        ]
