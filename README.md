
# A Basic TODO App

A Basic TODO App is made up of Django REST framework.


## Tech Stack
Python, Django, Django REST framework, Swagger, gunicorn, Docker, Heroku

  
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
  docker-compose up -d --build
```

  
## Feedback

If you have any feedback, please reach out to us at hello@amaharjan.com

  
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  
## Running Tests

To run tests, run the following command

```bash
  docker-compose exec web python manage.py test
```

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

  
## API Reference

### Login (admin)
[/api-auth/login/?next=/api/v1/](https://api-basic-todo-amaharjan.herokuapp.com/api-auth/login/?next=/api/v1/)

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

  