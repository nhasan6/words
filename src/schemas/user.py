from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str # only on create, never in response

class UserResponse(UserBase):
    id: int
    created_at: datetime
    model_config = {
        "from_attributes": True
    }

