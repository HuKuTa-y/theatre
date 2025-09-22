FROM python:3.12-slim

WORKDIR /src
COPY ["./", "./"]

RUN pip install --no-cache-dir requests python-telegram-bot

CMD ["uvicorn", "main:app", "--reload","--host","0.0.0.0", "--port","8080"]