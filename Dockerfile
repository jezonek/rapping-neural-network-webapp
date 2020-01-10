FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
COPY requirements-webapp.txt /app
RUN pip3 install -r requirements-webapp.txt
