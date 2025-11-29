# Planetarium API

API service for planetarium service realized on DRF

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
