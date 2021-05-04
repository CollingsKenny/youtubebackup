# Docker

Include in this directory playlist from google takeout called `likedvideoplaylist.csv`
Run docker container creation with `start.sh`

# Python scripts

## ytdown.py
This script simply downloads every video in an `likedvideoplaylist.csv` included in the directory.

`python3 ytdown.py`

## ytdown_mt.py
This script is a modification of ytdown.py that can be run using multiple threads.
Also, it will stop after donloading `MAX_COUNT` number of videos.
Will run a couple verification tests after the run is complete.

`python3 ytdown_mt.py DESTINATION [NUM_THREADS] [MAX_COUNT]`

## threaded_counter.py
This script is a proof of concept of the multithreading workflow that simply counts upwards to `MAX_COUNT`. This was written so that I could learn python multithreading without having to download videos. The main requirement that my workflow needed to insure is that **every number must be counted exactly once**. A few verification tests run in the script and will report if there are errors in my algorithm.

# Multithreading?
I noticed that when the videos are downloading there are two phases. First the video and audio download, then the two parts are packages them together. Each part of the phase uses different system resources, so potentially we could run multiple at a time. According to my very unscientific tests, each video completes about 10 seconds faster when using multithreading. When running on the ~600 videos I have in my likedvideoplaylist file, this should be signifcant time save.