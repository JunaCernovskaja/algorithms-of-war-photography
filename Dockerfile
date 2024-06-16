FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y unzip
RUN unzip /app/dataset/handpicked_dataset.zip -d /app/dataset/handpicked_dataset
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]