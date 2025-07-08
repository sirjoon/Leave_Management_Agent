from .session import SessionLocal
from app.models import user, leave, leave_balance, audit
from app.db.base import Base

def init_db():
    Base.metadata.create_all(bind=SessionLocal().get_bind())
