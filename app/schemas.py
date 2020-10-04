from pydantic import BaseModel
from typing import Dict


class PostBase(BaseModel):
    category: str
    sub_category: str
    owner: str
    photo: str
    address: str
    description: str
    support_cause: str

    class config:
        orm_mode = True
