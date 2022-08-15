from typing import List

from pydantic import BaseModel


class JumpcloudPagination(BaseModel):
    results: List
    total_count: int
