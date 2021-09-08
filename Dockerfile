From python:3.9

Run apt update && apt upgrade -y
Run apt install python3-pip -y
Run apt install ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD python3 -m player
Run pip3 install --upgrade pip
Run pip3 install -U -r requirements.txt

CMD python3 -m main.py
