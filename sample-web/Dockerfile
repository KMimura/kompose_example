FROM python:3.9

WORKDIR /
COPY requirements.txt /requirements.txt
COPY ./app /app

RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
