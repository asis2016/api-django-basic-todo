
# A Basic TODO App

A Basic TODO App is made up of Django REST framework.


## Tech Stack
Docker 20.10.6, Python 3.8, Django 3.2.3, Django REST framework, Whitenoise, Gunicorn, Heroku

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/asis2016/api-django-basic-todo.git
```

Go to the project directory

```bash
  cd api-django-basic-todo
```

Start the project

```bash
  docker build .
```

```bash
  docker-compose up -d --build
```

## Running Tests
To run tests, run the following command

```bash
  docker-compose exec web python manage.py test
```

  
## Environment Variables
`API_KEY` `django-insecure-*b-vg)^t=m2dtax_17)!zzbxmthz+o+p&^=k9_+)awgjy9(!l+`

## Django REST framework Docs
[/docs/](https://api-basic-todo-amaharjan.herokuapp.com/docs/)

### Django REST framework login API Login (as admin)
[/api-auth/login/?next=/api/v1/](https://api-basic-todo-amaharjan.herokuapp.com/api-auth/login/?next=/api/v1/)
- username: admin
- password: admin

  
## API Reference

#### Get all todos

```http
  GET /api/v1/
```

| Parameter | Type    
| :-------- | :-------
| `api_key` | `string`

#### Get todo

```http
  GET /api/v1/${uuid}
```

| Parameter | Type     
| :-------- | :------- 
| `uuid`      | `string` 

## Screenshots

### Django Administrator
[/admin/login/?next=/admin/](https://api-basic-todo-amaharjan.herokuapp.com/admin/login/?next=/admin/)

![Django Administrator login](/screenshots/admin-login.png)

### Django REST framework login API Login (as admin)
[/api-auth/login/?next=/api/v1/](https://api-basic-todo-amaharjan.herokuapp.com/api-auth/login/?next=/api/v1/)

![Django REST framework login](/screenshots/api-login.png)

### api/v1
[/api/v1/](https://api-basic-todo-amaharjan.herokuapp.com/api/v1/)

![/api/v1/](/screenshots/a.png)

### /api/v1/uuid
[/api/v1/076c5ced-b976-4835-9509-c82ec646b041](https://api-basic-todo-amaharjan.herokuapp.com/api/v1/076c5ced-b976-4835-9509-c82ec646b041)

![/api/v1/${id}](/screenshots/b.png)

### api/v1/rest-auth/registration/
To register as an user, register from the link below

[api/v1/rest-auth/registration/](https://api-basic-todo-amaharjan.herokuapp.com/api/v1/rest-auth/registration/)

![api/v1/rest-auth/registration/](/screenshots/c.png)


## Feedback
If you have any feedback, please reach out to us at hello@amaharjan.com