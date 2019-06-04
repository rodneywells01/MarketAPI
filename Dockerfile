FROM python:3.7

WORKDIR /app

# Dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ./scripts/run.sh
