from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
import enum

class LeaveStatus(str, enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
    cancelled = "Cancelled"

class LeaveRequestCreate(BaseModel):
    leave_type: str
    start_date: date
    end_date: date
    comments: Optional[str]

class LeaveRequestRead(BaseModel):
    id: int
    leave_type: str
    start_date: date
    end_date: date
    status: str
    requested_at: datetime
    approved_by: Optional[int]
    approved_at: Optional[datetime]
    comments: Optional[str]
    class Config:
        orm_mode = True
