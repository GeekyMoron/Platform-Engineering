FROM python:3.14-slim-trixie

COPY ./requirement.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

CMD ["python", "/app/src/app.py"]


