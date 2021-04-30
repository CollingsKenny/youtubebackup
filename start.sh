docker build --tag yt-dl .
docker run -v "$(pwd)/download:/data" yt-dl