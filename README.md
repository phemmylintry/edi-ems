# EDI Employee Management System

The assignment is to write a fictional company's employee management system. This company is
organized in separate teams of employees with one team leader per team. Every employee has an
hourly rate they get paid for their work. Not everybody in the company is a full time employee. Team
leaders are paid an additional 10% for their work.
Create an API which lets the company's accountant retrieve the list of employees with their respective
pay for the month.

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
