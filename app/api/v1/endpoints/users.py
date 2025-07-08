from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.db.session import SessionLocal
from app.api.v1.endpoints.auth import get_db
from app.core.security import decode_access_token
from fastapi import Header

router = APIRouter()

def get_current_user(token: str = Header(..., alias="Authorization"), db: Session = Depends(get_db)):
    if token.startswith("Bearer "):
        token = token[7:]
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = crud.crud_user.get_by_email(db, payload["sub"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/me", response_model=schemas.user.UserRead)
def read_users_me(current_user: models.user.User = Depends(get_current_user)):
    return current_user
