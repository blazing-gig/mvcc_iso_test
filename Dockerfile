
FROM python:3.7

RUN mkdir /code

WORKDIR /code

COPY . .

RUN python -m venv venv

RUN source venv/bin/activate

RUN pip install -r requirements.txt



