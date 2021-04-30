FROM python:3
RUN apt update -y && apt install -y \
    ffmpeg \
    atomicparsley
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "ytdown.py"]