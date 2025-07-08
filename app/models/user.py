import enum
from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base

class UserRole(str, enum.Enum):
    employee = "Employee"
    manager = "Manager"
    admin = "Admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.employee)
    department = Column(String, nullable=True)
