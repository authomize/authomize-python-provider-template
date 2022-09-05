from typing import Iterable


def get_paginated_results(api_function:classmethod) -> Iterable[object]:
    cur_skip = 0
    has_next = True
    while (has_next):
        api_response = api_function(skip=cur_skip)
        has_next = api_response.has_next
        cur_skip += int(api_response.next_skip)
        yield from api_response.records

def get_paginated_results_by_id(id:float, api_function_by_id:classmethod) -> Iterable[object]:
    cur_skip = 0
    has_next = True
    while (has_next):
        api_response = api_function_by_id(id, skip=cur_skip)
        has_next = api_response.has_next
        cur_skip += int(api_response.next_skip)
        yield from api_response.records
