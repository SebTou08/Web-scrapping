# Usar una imagen base de Python
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wget gnupg2
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.js"]
