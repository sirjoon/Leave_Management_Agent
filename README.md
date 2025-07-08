# Leave Management System

A FastAPI-based REST API to manage leave requests, users, and reporting.

## Features
- User management with JWT authentication
- Leave request creation, approval, rejection, cancellation
- Leave balances
- Simple reporting

## Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run database migrations
```bash
alembic upgrade head
```

### 3. Start the application
```bash
docker-compose up --build
```

The API will be available at http://localhost:8000

### 4. Access API docs
Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Project Structure
- `app/` - Main application code
- `alembic/` - Database migrations
- `tests/` - Pytest tests

## Environment Variables
See `app/core/config.py` for configuration options.

---
# Leave_Management_Agent
