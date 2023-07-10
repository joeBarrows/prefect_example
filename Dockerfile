FROM python:3.10

WORKDIR /app

COPY src/python3.10 /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4200

CMD ["python", "main.py"]

