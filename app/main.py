from fastapi import FastAPI
from app.api.v1.endpoints import auth, users, leaves, reports

app = FastAPI(title="Leave Management System")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(leaves.router, prefix="/api/v1/leaves", tags=["leaves"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["reports"])
