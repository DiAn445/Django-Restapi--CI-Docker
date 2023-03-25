FROM python:3.10.1


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Dj

COPY ./requirements.txt /Dj/requirements.txt


RUN pip install -r /Dj/requirements.txt

COPY . /Dj/

EXPOSE 8000
CMD ["python", "./Django_cats/manage.py", "runserver", "0.0.0.0:8000"]