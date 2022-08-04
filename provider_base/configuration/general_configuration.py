from pydantic import BaseModel


class GeneralConfiguration(BaseModel):
    batch_size: int = 100
