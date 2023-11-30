FROM python

COPY . /app

WORKDIR /app

RUN pip install flask

RUN pip install mysql-connector-python

RUN pip install python-dotenv

EXPOSE 5001

CMD ["python", "/app/script.py"]
