# FastAPI-projects
A growing collection of FastAPI backend projects exploring API development, databases, and full-stack applications.

# Inventory API (FastAPI + React)

A simple full-stack inventory management system built with FastAPI (backend), PostgreSQL (database), and React (frontend).

## Features
- Create, read, update, and delete products
- REST API built with FastAPI
- PostgreSQL database integration using SQLAlchemy
- React frontend connected via API
- CORS enabled for frontend-backend communication

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- React
- JavaScript (Frontend)
- Python (Backend)

## Architecture Overview

React → FastAPI (REST API) → SQLAlchemy ORM → PostgreSQL

## Project Structure

```bash
backend/
│── main.py
│── models.py
│── database.py
│── database_models.py

frontend/
│── (React app)
```

## Frontend

This project uses a React frontend originally based on:
https://github.com/navinreddy20/fastapi-demo/tree/products-with-ui/frontend

The frontend was slightly modified to work with a custom FastAPI + PostgreSQL backend implemented in this repository.

## How to Run

### Backend
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
uvicorn main:app --reload
```
### Frontend
```bash
npm install
npm start
```

## API Endpoints
- GET `/products` → Retrieve all products
- GET `/products/{id}` → Retrieve a single product
- POST `/products` → Create a product
- PUT `/products/{id}` → Update a product
- DELETE `/products/{id}` → Delete a product

## Notes
- Backend runs locally on PostgreSQL
- Frontend runs on localhost:3000

## What I Learned
- Building REST APIs with FastAPI
- ORM usage with SQLAlchemy
- Connecting frontend and backend via HTTP
- Handling CORS issues between React and FastAPI
- PostgreSQL integration in a Python backend