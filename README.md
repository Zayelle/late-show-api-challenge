# 🌙 Late Show API

A Flask REST API to manage guests, episodes, and appearances on a late-night show — featuring PostgreSQL, token-based auth (JWT), and fully testable routes.

---

## 📦 Tech Stack

- Flask (REST API)
- PostgreSQL (mandatory DB)
- SQLAlchemy + Flask-Migrate
- Flask-JWT-Extended (JWT auth)
- Postman (for testing)

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

git clone https://github.com/Zayelle/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies

pipenv install
pipenv shell
```

### 3. PostgreSQL Setup
Create the database in Postgres:
```sql
CREATE DATABASE late_show_db;
```

### 4. Set Environment Variables  
Create a `.env` file in the root with:
```env
DATABASE_URI=postgresql://<user>:<password>@localhost:5432/late_show_db
JWT_SECRET_KEY=super-secret-key
FLASK_APP=server/app.py
FLASK_ENV=development
```

---

## 🚀 Running the App

### Run Migrations

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Seed the Database

python server/seed.py
```

### Start the Server

flask run
```

---

## 🔐 Auth Flow

### 1. Register
```http
POST /register
Content-Type: application/json
{
  "username": "admin",
  "password": "password123"
}
```

### 2. Login
```http
POST /login
Content-Type: application/json
{
  "username": "admin",
  "password": "password123"
}
```

Response:
```json
{ "access_token": "<JWT_TOKEN>" }
```

### 3. Use the Token
Include this header in protected requests:
```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📡 Routes & Examples

| Route                    | Method | Auth? | Description                           |
|--------------------------|--------|-------|-------------------------------------- |
| `/register`              | POST   | ❌     | Register a user                      |
| `/login`                 | POST   | ❌     | Log in and receive JWT token         |
| `/guests`                | GET    | ❌     | List all guests                      |
| `/episodes`              | GET    | ❌     | List all episodes                    |
| `/episodes/<id>`         | GET    | ❌     | Get episode with appearances         |
| `/episodes/<id>`         | DELETE | ✅     | Delete episode (requires JWT)        |
| `/appearances`           | POST   | ✅     | Create appearance (requires JWT)     |

### Example: Create Appearance
```http
POST /appearances
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json
{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 5
}
```

---

## 🧪 Postman Usage

1. Open Postman → **Import**
2. Choose: `challenge-4-lateshow.postman_collection.json`
3. Set `jwt_token` variable after login:
   - Go to "Variables" → paste your token under `jwt_token`
4. Use pre-written requests:
   - Register, login, get episodes, delete, post appearance, etc.

---

## 🔗 GitHub Repo

> 📁 [https://github.com/Zayelle/late-show-api-challenge.git](https://github.com/Zayelle/late-show-api-challenge.git)