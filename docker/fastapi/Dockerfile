FROM python:3.7-stretch
WORKDIR /usr/src
COPY requirements.txt .
# package install
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]