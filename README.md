# Planetarium API

API service for planetarium service realized on DRF


# Features

- JWT authentication system
- Admin panel available at /admin/
- API documentation with Swagger at /api/doc/swagger/
- Managing reservations and tickets
- Creating astronomy shows with themes
- Creating planetarium domes with capacity management
- Adding show sessions with scheduling
- Filtering astronomy shows by title and themes
- Filtering show sessions by date and show
- User registration and profile management
- Ticket validation and seat allocation system
- Image upload for astronomy shows and domes
- Role-based access control (User/Admin)

## Installing using GitHub

Install PostgresSQL and create db

```bash
git clone https://github.com/iivitalik/py-planetarium-service.git
cd py-planetarium-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# For Windows:
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>

# For Linux/Mac:
export DB_HOST=<your db hostname>
export DB_NAME=<your db name>
export DB_USER=<your db username>
export DB_PASSWORD=<your db user password>
export SECRET_KEY=<your secret key>

python manage.py migrate
python manage.py runserver
python manage.py runserver  
```


# Run with docker

Docker should be installed  
```bash
docker-compose build  
docker-compose up  
```

# Getting access

- create user via /api/user/register/  
- get access token via /api/user/token/

# Pages images

### 🔐 Authentication & Documentation
<div align="center">

| Swagger | JWT Authentication | Admin Panel |
|:---:|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/3a5dfe02-b6c4-42f7-9ad0-a2e4346079a7" width="250"> | <img src="https://github.com/user-attachments/assets/31eaadd2-a510-4709-8275-67340dc43ad9" width="250"> | <img src="https://github.com/user-attachments/assets/eec74532-f788-41ff-b531-423d40fe6798" width="250"> |

</div>

### 🎭 Content & Booking
<div align="center">

| Main API | Astronomy Shows | Show Sessions | Reservations |
|:---:|:---:|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/542a6eaa-7fc2-4972-8fdf-5babc9ff67b6" width="200"> | <img src="https://github.com/user-attachments/assets/c2a9717e-d03f-44b3-a300-bcee205e5f11" width="200"> | <img src="https://github.com/user-attachments/assets/75b3f9c9-ab26-4467-bd0b-4338a8d52b15" width="200"> | <img src="https://github.com/user-attachments/assets/b86df76a-0776-4e7c-9ab6-574090ad06c0" width="200"> |

</div>
