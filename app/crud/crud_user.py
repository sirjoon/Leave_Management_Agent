from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.core.security import get_password_hash
from app.schemas.user import UserCreate

class CRUDUser:
    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, obj_in: UserCreate):
        db_user = User(
            name=obj_in.name,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            role=obj_in.role,
            department=obj_in.department,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

crud_user = CRUDUser()
