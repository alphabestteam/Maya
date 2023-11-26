FROM python
RUN pip3 install Flask
COPY ./dep/app1.py ./app/app.py
EXPOSE 5001
WORKDIR /app
CMD python3 app.py