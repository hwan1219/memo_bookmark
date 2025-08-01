from typing import Optional, List
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr, ConfigDict 
from memo import Memo
from bookmark import Bookmark

class User(SQLModel, table=True):
  id: Optional[int] = Field(default=None, primary_key=True)
  username: str = Field(index=True, unique=True)
  hashed_password: str
  nickname: Optional[str] = Field(default="unknown")
  email: Optional[EmailStr] = Field(default=None, unique=True)
  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
  
  memos: List[Memo] = Relationship(back_populates="owner")
  bookmarks: List[Bookmark] = Relationship(back_populates="owner")


# 스키마
class UserBase(SQLModel):
  nickname: Optional[str] = Field(default="unknown", max_length=8)
  email: Optional[EmailStr] = Field(default=None)
  model_config = ConfigDict(extra='forbid')
  
class UserCreate(UserBase):
  username: str = Field(min_length=4, max_length=30)
  password: str = Field(min_length=6)
  auth_code: str

class UserUpdate(UserBase):
  pass

class UserPasswordUpdate(SQLModel):
  current_password: str = Field(min_length=6)
  new_password: str = Field(min_length=6)
  new_password_confirm: str = Field(min_length=6)
  model_config = ConfigDict(extra='forbid')

class UserBasicInfo(UserBase):
  id: int
  model_config = {"from_attributes": True}