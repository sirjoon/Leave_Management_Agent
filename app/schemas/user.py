from pydantic import BaseModel, EmailStr
from typing import Optional
import enum

class UserRole(str, enum.Enum):
    employee = "Employee"
    manager = "Manager"
    admin = "Admin"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole = UserRole.employee
    department: Optional[str]

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    class Config:
        orm_mode = True
