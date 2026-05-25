from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    age: int
    salary: Optional[float]
    created_at: Optional[date]
