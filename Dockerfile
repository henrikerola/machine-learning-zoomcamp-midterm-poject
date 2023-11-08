FROM python:3.10-bullseye
 
WORKDIR /app
 
RUN pip install --no-cache flask==3.0.0 gunicorn==21.2.0 pandas==2.1.2 scikit-learn==1.3.2

COPY . .
 
EXPOSE 80

CMD [ "gunicorn", "--bind=0.0.0.0:80", "predict:app" ]