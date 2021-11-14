FROM python:3.10-slim-bullseye
WORKDIR /usr/src
COPY requirements.txt .
# package install
# python3.10ではmysqlclientの利用にgcc及びlibmariadb-devが必要
RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]