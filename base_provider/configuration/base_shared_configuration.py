from pydantic import BaseModel


class SharedConfiguration(BaseModel):
    log_extactor_every_n_raw_items: int = 100
    log_transformer_every_n_raw_items: int = 100
