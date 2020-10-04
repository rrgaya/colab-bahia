from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, Integer, String
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid4)
    category = Column(String)
    sub_category = Column(String)
    owner = Column(String)
    photo = Column(String)
    address = Column(String)
    description = Column(String)
    support_case = Column(Integer)
