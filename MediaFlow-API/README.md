# MediaFlow API

A lightweight media-sharing backend built with **FastAPI**, supporting user authentication, image/video uploads, and a simple feed system.

The project uses **ImageKit** for media storage and **SQLite** as the database.

---


## 🚀 Features

- User authentication (JWT-based)
- User registration, login, password reset (via FastAPI Users)
- Upload images and videos
- Cloud media storage via ImageKit
- Feed endpoint with user ownership metadata
- Delete posts (owner-only access)
- Async database operations with SQLAlchemy
- Simple frontend for testing API

---


## 🧱 Tech Stack

- FastAPI
- SQLAlchemy (Async)
- SQLite
- FastAPI Users
- ImageKit.io
- Python 3.12+
- Uvicorn
- aiosqlite

---


## 📁 Project Structure

- app/
    - app.py              # Main FastAPI application
    - db.py               # Database models & session
    - users.py            # Authentication logic (FastAPI Users)
    - images.py           # ImageKit configuration
    - schemas.py          # Pydantic schemas

- frontend.py             # Simple frontend (adapted from Tech With Tim)
- main.py                 # App entry point

---


## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/aylinasadi/FastAPI-projects.git
cd "FastAPI-projects/MediaFlow API"
```
### 2. Create environment (uv)
```bash
uv venv
uv sync
```
### 3. Run the server
```bash
uv run uvicorn main:app --reload
```

## 🔐 Environment Variables

Create a .env file in the root directory:

```env
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_URL_ENDPOINT=your_url_endpoint
JWT_SECRET=your_secret_key
```


## 📡 API Endpoints

- Authentication
    - POST /auth/register → Create account
    - POST /auth/jwt/login → Login
    - POST /auth/jwt/logout → Logout
- Users
    - GET /users/me → Get current user
- Media
    - POST /upload → Upload image/video
    - GET /feed → Get all posts
    - DELETE /post/{post_id} → Delete a post (owner only)


## 🖥 Frontend

Frontend adapted from Tech With Tim:
https://github.com/techwithtim/FastAPIPhotoVideoSharing/blob/main/frontend.py


## 🗄 Database

- Uses SQLite
- File: test.db
- Tables are automatically created on startup using FastAPI lifespan events


## ⚠️ Notes

- Media files are stored on ImageKit, not locally
- Temporary upload files are deleted automatically after processing
- Authentication is required for uploading, viewing user data, and deleting posts
- Feed endpoint includes ownership metadata (is_owner, user info)