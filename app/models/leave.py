import enum
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class LeaveStatus(str, enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
    cancelled = "Cancelled"

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    leave_type = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum(LeaveStatus), default=LeaveStatus.pending)
    requested_at = Column(DateTime)
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    comments = Column(String, nullable=True)

    requester = relationship("User", foreign_keys=[user_id])
    approver = relationship("User", foreign_keys=[approved_by])
