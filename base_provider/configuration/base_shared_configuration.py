from pydantic import BaseModel


class BaseSharedConfiguration(BaseModel):
    loader_batch_size: int = 100
    loader_log_every_n_raw_items: int = 100
    log_extactor_every_n_raw_items: int = 100
    transformer_log_every_n_raw_items: int = 100
