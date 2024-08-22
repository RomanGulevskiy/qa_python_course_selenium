FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]