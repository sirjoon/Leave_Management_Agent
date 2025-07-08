from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from app.db.base import Base

class LeaveBalance(Base):
    __tablename__ = "leave_balances"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    leave_type = Column(String, nullable=False)
    balance_days = Column(Float)
    updated_at = Column(DateTime)
