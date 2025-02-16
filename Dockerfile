FROM python:3.9

WORKDIR /app

COPY app/ app/
COPY templates/ templates/
COPY static/ static/

RUN pip install -r app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
