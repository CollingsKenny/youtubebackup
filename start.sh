# docker volume create --driver local \
#     --opt type=cifs \
#     --opt device='//192.168.1.210/kennysbox' \
#     --opt o='username=kennysbox,password=kennysbox' \
#     downloadvolume

docker build --tag yt-dl .
docker run -v "$(pwd):/data" yt-dl 
# docker run -v downloadvolume:/data yt-dl
# docker run --mount type=volume,source=downloadvolume,target=/data yt-dl
