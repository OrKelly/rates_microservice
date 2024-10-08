FROM python:3.9

RUN mkdir /rates

WORKDIR /rates

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /rates/entrypoint.sh

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker","--bind=0.0.0.0:8000"]