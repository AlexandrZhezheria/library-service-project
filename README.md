# Book Borrow API

API service for library management written on DRF

## Installing using GitHub

Install PostgresSQL and create db

```shell
git clone https://github.com/AlexandrZhezheria/library-service-project.git
cd library-service-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

create file .env with vars:  # Set Environment Variables like in file .env.sample
DJANGO_SECRET_KEY=<your Django secret key>
POSTGRES_HOST=<your db hostname>
POSTGRES_DB=<your db name>
POSTGRES_USER=<your db username>
POSTGRES_PASSWORD=<your db user password>

python manage.py migrate
python manage.py runserver  # starts Django server
```


## Getting access

* create user via /api/users/
* get access token via /api/users/token/
* you can see API documentation via /api/doc/swagger/
