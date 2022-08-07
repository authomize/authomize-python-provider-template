from typing import Iterable

from base_provider.extractors.base_extactor import Extractor


class FilesExtactor(Extractor):
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
