FROM python:3.10.1-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "flask", "run", "-h", "0.0.0.0"]