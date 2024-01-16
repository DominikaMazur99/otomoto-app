FROM python:3.10-slim

WORKDIR /app

COPY ci/requirements/requirements.txt .

ENV PIP_INDEX_URL=https://pypi.org/simple

RUN python -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

RUN apt update && apt install -y tree

COPY . .

# Add these lines to initialize the database and apply migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Update this line to start the development server
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
