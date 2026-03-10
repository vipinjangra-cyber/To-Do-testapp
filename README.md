# Todo App (Docker + FastAPI + PostgreSQL)

A simple full-stack Todo application built using **FastAPI**, **PostgreSQL**, and **Docker**.
This project demonstrates how to run a **multi-container application** using Docker Compose.

The application allows users to:

* Add tasks
* Mark tasks as completed
* Delete tasks
* View all tasks

---

# Architecture

The application consists of three main services:

Browser
↓
Frontend (Nginx container)
↓
Backend API (FastAPI container)
↓
PostgreSQL Database container

The services communicate through a Docker network managed by Docker Compose.

---

# Tech Stack

Backend

* FastAPI
* SQLAlchemy
* Python

Frontend

* HTML
* CSS
* JavaScript
* Nginx

Database

* PostgreSQL

Infrastructure

* Docker
* Docker Compose

---

# Project Structure

TO-DO-testapp

docker-compose.yml

frontend
├── Dockerfile
├── index.html
├── script.js
└── style.css

backend
├── Dockerfile
├── main.py
├── database.py
├── model.py
└── requirement.txt

.gitignore
README.md

---

# Prerequisites

Before running the project make sure you have installed:

* Docker
* Docker Compose

Verify installation:

docker --version
docker compose version

---

# Running the Application

Clone the repository:

git clone https://github.com/your-username/todo-app.git

cd todo-app

Build and start all services:

docker compose up --build

Run in background:

docker compose up -d

---

# Access the Application

Frontend

http://localhost:8080

Backend API

http://localhost:8000

List Tasks

http://localhost:8000/tasks

---

# API Endpoints

GET /tasks
Returns all tasks.

POST /tasks
Creates a new task.

PUT /tasks/{task_id}
Marks a task as completed.

DELETE /tasks/{task_id}
Deletes a task.

---

# Database Configuration

The backend connects to PostgreSQL using:

postgresql://todouser:1234@db:5432/tododb

Docker Compose automatically creates the network so the backend can access the database using the hostname `db`.

---

# Useful Docker Commands

Start services

docker compose up

Start in background

docker compose up -d

Stop services

docker compose down

View logs

docker compose logs -f

List running containers

docker compose ps

---

# Learning Goals

This project demonstrates:

* Building REST APIs with FastAPI
* Using SQLAlchemy ORM
* Connecting FastAPI with PostgreSQL
* Containerizing applications using Docker
* Running multi-container applications using Docker Compose
* Basic frontend integration with backend APIs

---

# Future Improvements

Possible improvements for this project:

* Add authentication (JWT)
* Add task editing
* Add user accounts
* Add Nginx reverse proxy
* Add monitoring using Prometheus and Grafana
* Deploy on cloud platforms (AWS / DigitalOcean)

---

# Author

Vipin Jangra

DevOps / Cloud / Backend Learning Project
