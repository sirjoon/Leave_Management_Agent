from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.db.session import SessionLocal
from app.api.v1.endpoints.users import get_current_user, get_db

router = APIRouter()

@router.post("/request", response_model=schemas.leave.LeaveRequestRead)
def create_leave_request(
    leave_in: schemas.leave.LeaveRequestCreate,
    db: Session = Depends(get_db),
    current_user: models.user.User = Depends(get_current_user),
):
    leave = crud.crud_leave.create(db=db, obj_in=leave_in, user_id=current_user.id)
    return leave

@router.post("/approve/{leave_id}")
def approve_leave(leave_id: int, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    leave = crud.crud_leave.approve(db, leave_id, current_user.id)
    if not leave:
        raise HTTPException(status_code=404, detail="Leave not found")
    return leave

@router.post("/reject/{leave_id}")
def reject_leave(leave_id: int, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    leave = crud.crud_leave.reject(db, leave_id, current_user.id)
    if not leave:
        raise HTTPException(status_code=404, detail="Leave not found")
    return leave

@router.post("/cancel/{leave_id}")
def cancel_leave(leave_id: int, db: Session = Depends(get_db), current_user: models.user.User = Depends(get_current_user)):
    leave = crud.crud_leave.cancel(db, leave_id, current_user.id)
    if not leave:
        raise HTTPException(status_code=404, detail="Leave not found or not owned by user")
    return leave
