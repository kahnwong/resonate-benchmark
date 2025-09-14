from datetime import datetime

from pydantic import BaseModel


class ResponseItem(BaseModel):
    time: datetime
    message: str
