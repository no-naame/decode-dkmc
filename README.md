# DKMC Backend - FastAPI Template

A FastAPI template with async SQLAlchemy, structured for scalability.

## Project Structure

```
dkmc_backend1/
├── app/
│   ├── core/
│   │   ├── config.py        # Settings, env vars
│   │   └── database.py      # SQLAlchemy async engine + session
│   ├── tools/
│   │   └── milestones/      # Feature module
│   │       ├── routes/
│   │       │   └── endpoints.py
│   │       ├── models.py
│   │       ├── schemas.py
│   │       ├── services.py
│   │       └── utils.py
│   └── main.py              # FastAPI app entrypoint
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Run the application:
```bash
python -m app.main
```

Or with uvicorn directly:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation
- `GET /api/v1/milestones/` - Get all milestones
- `POST /api/v1/milestones/` - Create milestone
- `GET /api/v1/milestones/{id}` - Get milestone by ID
- `PUT /api/v1/milestones/{id}` - Update milestone
- `DELETE /api/v1/milestones/{id}` - Delete milestone

## Features

- ✅ FastAPI with async support
- ✅ SQLAlchemy with async engine
- ✅ Pydantic for data validation
- ✅ Structured project layout
- ✅ Environment configuration
- ✅ CORS middleware
- ✅ Health check endpoint
- ✅ Interactive API docs
