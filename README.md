# Student Database Project

A beginner-friendly starting point for the EWB internship assignment.

## Requirements
- Python 3
- Visual Studio Code

## Setup
Open a terminal in this folder and run:

```bash
python -m venv .venv
.venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

Open these addresses in your browser:
- API home: http://127.0.0.1:8000/
- Interactive API docs: http://127.0.0.1:8000/docs

## Current status
This is the starter version. It confirms FastAPI is running. We will add SQLite and the four student CRUD operations together in the next stages.
