# Job Application Management API (Django REST)

A backend REST API for a job application platform (similar to a simplified LinkedIn Jobs),
built using Django and Django REST Framework.

This project focuses on **backend architecture, authentication, authorization, and clean API design**.

---

## Features

### Authentication
- User signup
- Login using JWT (access & refresh tokens)
- Logout (token-based / client-side)
- Role-based access (User vs Admin)

### Jobs
- List active job openings
- Jobs can be activated/deactivated by admin

### Applications
- Users can apply to a job **only once**
- Users can view their own applications
- Admin can:
  - View all applications
  - Update application status (applied / shortlisted / rejected)

### Security
- Protected endpoints using JWT authentication
- Permissions enforced at API level
- Business rules enforced at database level

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Database**: SQLite (development)
- **Language**: Python
- **Tools**: Postman (API testing)

---

## 📂 Project Structure (simplified)

