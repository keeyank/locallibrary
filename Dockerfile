FROM python:latest

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

# Specifying 0.0.0.0 as the IP address allows clients outside of the container
# to communicate with the server in the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]