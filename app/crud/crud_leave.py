from sqlalchemy.orm import Session
from app.models.leave import LeaveRequest, LeaveStatus
from app.schemas.leave import LeaveRequestCreate
from datetime import datetime

class CRUDLeave:
    def create(self, db: Session, obj_in: LeaveRequestCreate, user_id: int):
        leave = LeaveRequest(
            user_id=user_id,
            leave_type=obj_in.leave_type,
            start_date=obj_in.start_date,
            end_date=obj_in.end_date,
            status=LeaveStatus.pending,
            requested_at=datetime.utcnow(),
            comments=obj_in.comments,
        )
        db.add(leave)
        db.commit()
        db.refresh(leave)
        return leave

    def get(self, db: Session, leave_id: int):
        return db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

    def approve(self, db: Session, leave_id: int, approver_id: int):
        leave = self.get(db, leave_id)
        if leave:
            leave.status = LeaveStatus.approved
            leave.approved_by = approver_id
            leave.approved_at = datetime.utcnow()
            db.commit()
            db.refresh(leave)
        return leave

    def reject(self, db: Session, leave_id: int, approver_id: int):
        leave = self.get(db, leave_id)
        if leave:
            leave.status = LeaveStatus.rejected
            leave.approved_by = approver_id
            leave.approved_at = datetime.utcnow()
            db.commit()
            db.refresh(leave)
        return leave

    def cancel(self, db: Session, leave_id: int, user_id: int):
        leave = self.get(db, leave_id)
        if leave and leave.user_id == user_id:
            leave.status = LeaveStatus.cancelled
            db.commit()
            db.refresh(leave)
        return leave

crud_leave = CRUDLeave()
