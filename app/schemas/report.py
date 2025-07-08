from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReportQuery(BaseModel):
    user_id: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]

class LeaveReport(BaseModel):
    user_id: int
    total_leaves: int
    approved_leaves: int
    rejected_leaves: int
    pending_leaves: int
