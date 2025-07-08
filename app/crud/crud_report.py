from sqlalchemy.orm import Session
from app.models.leave import LeaveRequest, LeaveStatus
from app.schemas.report import ReportQuery, LeaveReport
from sqlalchemy import func

def get_leave_report(db: Session, query: ReportQuery):
    q = db.query(
        LeaveRequest.user_id,
        func.count().label("total_leaves"),
        func.sum(func.case([(LeaveRequest.status == LeaveStatus.approved, 1)], else_=0)).label("approved_leaves"),
        func.sum(func.case([(LeaveRequest.status == LeaveStatus.rejected, 1)], else_=0)).label("rejected_leaves"),
        func.sum(func.case([(LeaveRequest.status == LeaveStatus.pending, 1)], else_=0)).label("pending_leaves"),
    )
    if query.user_id:
        q = q.filter(LeaveRequest.user_id == query.user_id)
    if query.start_date:
        q = q.filter(LeaveRequest.start_date >= query.start_date)
    if query.end_date:
        q = q.filter(LeaveRequest.end_date <= query.end_date)
    q = q.group_by(LeaveRequest.user_id)
    return [LeaveReport(
        user_id=row.user_id,
        total_leaves=row.total_leaves,
        approved_leaves=row.approved_leaves,
        rejected_leaves=row.rejected_leaves,
        pending_leaves=row.pending_leaves,
    ) for row in q.all()]
