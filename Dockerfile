FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install uvicorn[standard]
EXPOSE 8000

CMD ["gunicorn", "ws_imp_dj.asgi:application","-k","uvicorn.workers.UvicornWorker", "--workers=2", "-b","0.0.0.0:8000"]

