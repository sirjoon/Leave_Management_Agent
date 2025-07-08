from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db.session import SessionLocal
from app.api.v1.endpoints.users import get_current_user, get_db

router = APIRouter()

@router.post("/report", response_model=list[schemas.report.LeaveReport])
def get_report(query: schemas.report.ReportQuery, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.crud_report.get_leave_report(db, query)
