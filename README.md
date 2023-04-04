
The aim was to make small project (internet shop), 
    and work with it by means of Docker/Rest-framework,
        to create GitHub actions and check out how it works.

## Installation

1. Clone the repository: `git clone https://github.com/username/project.git`
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`

## Usage

1. Start the server: `python manage.py runserver`
2. Open your web browser and go to `http://127.0.0.1:8000/`
3. Log in to the admin panel using the created superuser.
4. Create objects for the project in the admin panel.

## Dependencies

asgiref==3.6.0
Django==4.1.7
djangorestframework==3.14.0
Pillow==9.4.0
pytz==2022.7.1
sqlparse==0.4.3
tzdata==2022.7


## Testing

You can run tests with the command: `python manage.py test`

# github-actions.yml
https://github.com/github/docs/actions/workflows/github-actions.yml/badge.svg
