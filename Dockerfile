# Usar una imagen base de Python
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wget gnupg2
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
RUN wget -N https://chromedriver.storage.googleapis.com/121.0.6167.160/chromedriver_linux64.zip -P ~/ && \
    unzip ~/chromedriver_linux64.zip -d ~/ && \
    mv -f ~/chromedriver /usr/local/bin/chromedriver && \
    chown root:root /usr/local/bin/chromedriver && \
    chmod 0755 /usr/local/bin/chromedriver && \
    rm ~/chromedriver_linux64.zip


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
