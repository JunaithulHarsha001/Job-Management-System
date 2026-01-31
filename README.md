# Job Application Management API (Django REST)

A backend REST API for a job application platform (similar to a simplified LinkedIn Jobs),
built using Django and Django REST Framework.

This project focuses on **backend architecture, authentication, authorization, and clean API design**.

---

## Features

### Authentication
- User signup
- Login using token-based authentication
- Logout (token revocation)
- Role-based access control (User vs Admin)

### Jobs
- List active job openings
- Jobs can be activated/deactivated by admin

### Applications
- Users can apply to a job only once
- Users can view their own applications
- Admin can view all applications and update application status

### Security
- Protected endpoints using DRF authentication
- Permissions enforced at API level
- Business rules enforced at database level

## Tech Stack

- Backend: Django, Django REST Framework
- Authentication: DRF Token Authentication (JWT planned)
- Database: SQLite (development)
- Language: Python
- Tools: Postman

---
## Work In Progress

- [ ] JWT authentication (access & refresh tokens)
- [ ] Frontend integration
- [ ] Pagination & filtering
- [ ] API tests
- [ ] PostgreSQL
- [ ] Deployment



