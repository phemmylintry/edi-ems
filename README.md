# EDI Employee Management System

The assignment is to write a fictional company's employee management system. This company is
organized in separate teams of employees with one team leader per team. Every employee has an
hourly rate they get paid for their work. Not everybody in the company is a full time employee. Team
leaders are paid an additional 10% for their work.
Create an API which lets the company's accountant retrieve the list of employees with their respective
pay for the month.

## Live Demo
Link to live demo: https://ems.samorb.com/
Base API URL: https://ems.samorb.com/api/

## Technologies and Tools
- Django, Django Rest Framework, SQLite
- Docker, Docker Compose, Github, Github Actions
- Nginx, Gunicorn, DigitalOcean (Ubuntu 20.04)
- PyTest, Black, MyPy, Django Debug Toolbar

## Postman Documentation
Link to the Postman documentation: https://documenter.getpostman.com/view/11358975/2s84DkU4hJ#23cf3458-9b66-48f8-8268-5dd93a0342da

## Installation

Clone the project, create a virtual environment, install dependencies

```bash
https://github.com/phemmylintry/edi-ems.git
virtualenv env
pipx install poetry==1.2.1
poetry install
```

## Running the project locally

```bash
python manage.py migrate
python manage.py runserver
```

## Running with Docker

```bash
docker-compose up --build
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

Oluwafemi Adenuga phemmylintry@gmail.com
