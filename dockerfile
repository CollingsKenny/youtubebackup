FROM python:3
RUN apt update -y && apt install -y \
    ffmpeg \
    atomicparsley \
    cifs-utils
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# RUN mkdir /data && mount -t cifs -o username=kennysbox,password=kennysbox //192.168.1.210/kennysbox /data
ENTRYPOINT ["python3", "ytdown.py"]