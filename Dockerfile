FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install uvicorn[standard]
EXPOSE 8000

CMD ["daphne","-b","0.0.0.0","-p" ,"8000" ,"ws_imp_dj.asgi:application"]

