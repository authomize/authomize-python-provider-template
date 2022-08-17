from typing import Callable, List

from jumpcloud_provider.models.jumpcloud_pagination import JumpcloudPagination

JumpcloudApiResult = Callable[[int], JumpcloudPagination | List]
