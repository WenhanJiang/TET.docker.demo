FROM python:3.11
COPY ./app /app
RUN  pip3 install fastapi uvicorn
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","15400"]
