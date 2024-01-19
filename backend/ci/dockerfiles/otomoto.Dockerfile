FROM python:3.12-slim

WORKDIR /app


# Install build dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy requirements file separately to leverage Docker cache
COPY ci/requirements/requirements.txt .

# Install psycopg2-binary
RUN pip install psycopg2-binary==2.9.9  # Use the desired version

# Install other dependencies
RUN pip install -r requirements.txt

# Install tree
RUN apt-get update && apt-get install -y tree

# Copy the rest of the application code
COPY . .

# Set the entrypoint
ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:8000"]