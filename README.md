# 🚀 Project & Task Management API (Django REST Framework)

A **production-ready Project & Task Management REST API** built using **Django REST Framework (DRF)** with:

- ✅ JWT Authentication (Access + Refresh)
- ✅ Role-Based Access Control (Admin / Manager / User)
- ✅ Secure Queryset-Level Data Protection
- ✅ Real-world Project ↔ Task relationship
- ✅ Clean, scalable architecture

This project is designed to demonstrate **senior-level DRF concepts** and is suitable for **real-world applications and interviews**.

---

## 📌 Features

- 🔐 JWT Authentication (Login & Refresh)
- 👥 Role-based permissions:
  - **Admin** → Full access
  - **Manager** → Project & Task management
  - **User** → Read-only access to assigned projects
- 🏢 Company → Project → Task hierarchy
- 🔍 Users can see **only projects where they have tasks**
- ⚡ Optimized queries using `select_related` & `distinct()`
- 🧪 Postman-ready APIs

---

## 🏗️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite (Dev) / PostgreSQL (Production-ready)

---

## 📁 Project Structure


proj_task_mgmt_api/
│
├── proj_task_mgmt_api/
│ ├── settings.py
│ ├── urls.py
│
├── proj_mgmt_api/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── permissions.py
│ ├── signals.py
│ ├── urls.py
│
└── manage.py


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/project-task-management-api.git
cd project-task-management-api

Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install django djangorestframework djangorestframework-simplejwt

4️⃣ Database Setup
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver


Server will run at:

http://127.0.0.1:8000/

🔐 Authentication (JWT)
➤ Login (Get Tokens)

POST /api/auth/login/

{
  "username": "admin",
  "password": "admin123"
}


Response:

{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}

➤ Refresh Token

POST /api/auth/refresh/

{
  "refresh": "REFRESH_TOKEN"
}

➤ Use Token in Requests

Add Header in Postman:

Authorization: Bearer ACCESS_TOKEN

👥 User Roles & Permissions
Role	Projects	Tasks	Companies
Admin	Full Access	Full Access	Full Access
Manager	Full Access	Full Access	Read
User	Assigned Projects Only	Assigned Tasks	No Access
📡 API Endpoints
🔹 Company

GET /api/companies/

POST /api/companies/ (Admin only)

🔹 Projects

GET /api/projects/

POST /api/projects/ (Admin / Manager)

GET /api/projects/{id}/

🔹 Tasks

GET /api/tasks/

POST /api/tasks/

PATCH /api/tasks/{id}/

🧪 Sample Request Payloads
➤ Create Project
{
  "company": 1,
  "name": "HR Management System",
  "description": "Internal HR platform",
  "status": "active",
  "start_date": "2026-01-01",
  "end_date": "2026-06-30"
}

➤ Create Task
{
  "project": 1,
  "title": "Design database schema",
  "assigned_to": 2,
  "priority": "high",
  "status": "todo",
  "due_date": "2026-01-25"
}

🔒 Data Security Design

Permissions control who can access endpoints

get_queryset() controls what data is visible

Normal users see only projects where they are assigned tasks

Unauthorized data returns 403 / 404

🧠 Interview Highlights

You can confidently say:

“I implemented role-based access using JWT authentication, custom permissions, and queryset-level filtering to ensure no unauthorized data exposure.”

🚀 Future Enhancements

Swagger / OpenAPI documentation

Celery-based notifications

Company-level multi-tenancy

API test cases (pytest)

Docker support

📜 License

This project is open-source and free to use for learning and development.

👨‍💻 Author

Dattatraya Walunj
Backend Developer (Django / DRF)

⭐ If you like this project, give it a star on GitHub!


---

### ✅ What You Have Now
- ✔ Professional GitHub README  
- ✔ Interview-ready documentation  
- ✔ Clean & structured explanation  

If you want next, I can:
- Add **Swagger UI**
- Add **Docker support**
- Add **API tests**
- Add **deployment guide**

Just tell me 👍
