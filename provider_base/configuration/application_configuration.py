from pydantic import BaseModel


class ApplicationConfiguration(BaseModel):
    app_id: str
