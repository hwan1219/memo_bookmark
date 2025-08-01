from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship
from pydantic import ConfigDict
from user import User

class Memo(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  title: str
  content: str
  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  
  user_id: int = Field(foreign_key="users.id", index=True, nullable=False)
  owner: "User" = Relationship(back_populates="memos")


# 스키마  
class MemoBase(SQLModel):
  title: str = Field(min_length=1, max_length=50)
  content: str = Field(min_length=1, max_length=10000)
  model_config = ConfigDict(extra='forbid')

class MemoCreate(MemoBase):
  pass

class MemoUpdate(MemoBase):
  pass

class MemoRead(MemoBase):
  id: int
  created_at: datetime
  model_config = {"from_attributes": True}