FROM python:3.12-alpine
WORKDIR /tests
COPY ../requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN apt update && apt install -y netcat-traditional
COPY . .
RUN chmod +x wait-for-it.sh
CMD ["pytest"]