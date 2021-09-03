From python:3.9

Run apt update && apt upgrade -y
Run apt install python3-pip -y
Run apt install ffmeg -y

WORKDIR /shubham

Run pip3 install --upgrade pip
Run pip3 install -U -r requirements.txt

CMD python3 -m main.py
