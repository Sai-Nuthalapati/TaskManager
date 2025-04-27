<<<<<<< HEAD
# 🧠 TaskManager API

A Unix-inspired task management API built with Django and Django REST Framework. Mimics commands like `ls`, `fork`, `rm`, and `put` for managing tasks via RESTful endpoints. 

---

## 🚀 Features

- `GET /tasks/` – List all tasks (like `ls`)
- `POST /tasks/` – Create a new task
- `GET /tasks/<id>/` – Retrieve a task
- `PUT /tasks/<id>/` – Update a task
- `DELETE /tasks/<id>/` – Delete a task (like `rm`)
- `POST /tasks/<id>/fork/` – Duplicate a task (like Unix `fork`)

---

## 🛠 Tech Stack

- **Python 3.11+**
- **Django 5.2**
- **Django REST Framework**
- **SQLite (default)**

---

## 📦 Installation

```bash
git clone https://github.com/Sai-Nuthalapati/TaskManager.git
cd TaskManager
python -m venv .venv
.venv\Scripts\activate   # On Windows
```

---

## ⚙️ Migrations & Run Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔍 Example Usage with `curl`

### Create a Task
```bash
curl -X POST http://127.0.0.1:8000/tasks/ \
 -H "Content-Type: application/json" \
 -d "{\"name\": \"My Task\", \"description\": \"Something to do\", \"status\": \"running\"}"
```

### Response:
```json
{
  "id": 1,
  "name": "My Task",
  "description": "Something to do",
  "status": "running",
  "created_at": "2025-04-22T20:00:00Z"
}
```

### Fork a Task
```bash
curl -X POST http://127.0.0.1:8000/tasks/1/fork/
```

### Update a Task
```bash
curl -X PUT http://127.0.0.1:8000/tasks/1/ \
 -H "Content-Type: application/json" \
 -d "{\"name\": \"Updated Task\", \"description\": \"New desc\", \"status\": \"completed\"}"
```

### Delete a Task
```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1/
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

Test cases verify key functionality like task forking, updates, and deletions.

---

## 📂 Project Structure

```
TaskManager/
├── manage.py
├── TaskManager/
│   └── settings.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── tests.py
```

---

## 📌 Notes

- This API is for demonstration purposes; it has no authentication or permissions yet.
- `fork` behavior is implemented in a custom endpoint using Django REST Framework views.
- SQLite is used for simplicity and ease of local development.

---


## 👨‍💻 Author

Made with ☕ by Nuthalapati Sai Sethu
=======
# TaskManager
Unix-inspired task management API
>>>>>>> 61fc0d47b6f8c5fb6e2a24f8d45b4d107e121388
