Features
User registration and login with hashed password storage

JWT-based authentication using OAuth2 (Bearer tokens)

Create, retrieve, update, and delete personal tasks

Authorization enforced on all task routes

PostgreSQL database integration via SQLAlchemy ORM

Environment configuration with .env and python-dotenv

Tech Stack
Framework: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Authentication: OAuth2 + JWT (python-jose)

Password Hashing: Passlib (bcrypt)

Environment Management: python-dotenv

Folder Structure
task-pilot/
│
├── app/
│   ├── auth.py         # Auth endpoints and token logic
│   ├── tasks.py        # Task CRUD routes
│   ├── models.py       # SQLAlchemy ORM models
│   ├── schemas.py      # Pydantic schemas
│   ├── database.py     # DB connection setup
│
├── main.py             # App entry point
├── .env                # Environment variables
├── requirements.txt

pip install -r requirements.txt
Configure your .env file with:


DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<database>
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Run the application:
uvicorn main:app --reload
API Endpoints
Auth Routes (/auth)
POST /auth/register: Register a new user

POST /auth/login: Authenticate user and receive JWT token

Task Routes (/tasks)
All routes require Authorization: Bearer <token> header.

POST /tasks/: Create a new task

GET /tasks/: Retrieve all tasks for the authenticated user

GET /tasks/{id}: Retrieve a specific task

PUT /tasks/{id}: Update a task

DELETE /tasks/{id}: Delete a task

