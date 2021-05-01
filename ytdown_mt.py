#! /usr/bin/python3

"""
KennyC 05.01.21

USAGE:
  python3 ytdown_mt.py DESTINATION [NUM_THREADS] [MAX_COUNT]
"""

import youtube_dl
import csv
import threading
import timeit
import sys

start = timeit.default_timer()

# GLOBALS
counter = 0     # Index in the videos list for execution
report = []     # List of completed indexes, used to verifiy what was downloaded
videos = []     # List of video IDs

# Main Thread
#  Selectes an index from the global counter
#  Downloads the video at the index


class downloadingThread(threading.Thread):
    def __init__(self, threadID, name, maxCount):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.maxcount = maxCount

    def run(self):
        global counter
        global report

        print(self.name, "Started")
        while True:
            # Select  counter, then increment for the next thread
            threadLock.acquire()

            myCount = counter
            if myCount > self.maxcount:
                print(self.name, "Finished")
                threadLock.release()
                break
            counter += 1

            threadLock.release()

            # Execute
            print(self.name, "ytdl", videos[myCount])
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([videos[myCount]])
            report.append(myCount)


# Read in Video IDs
print("Reading likedvideoplaylist.csv")
with open('likedvideoplaylist.csv', newline='') as csvfile:
    csvlist = list(csv.reader(csvfile, delimiter=','))
    for row in csvlist[5:]:
        if len(row) >= 0:
            videos.append(row[0])

# COMMAND LINE ARGUMENTS
#   (validation method: crap in crap out)
destination = sys.argv[1]
numThreads = 2
maxCount = 100

if len(sys.argv) > 2:
    numThreads = int(sys.argv[2])
if len(sys.argv) > 3:
    maxCount = int(sys.argv[3])
    if maxCount > len(videos):
        maxCount = len(videos)


ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
    'outtmpl': destination + '/%(title)s.%(ext)s',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ]
}

print("Starting program with", numThreads,
      "threads, downloading ", maxCount, "videos ...")

# THREADS
threadLock = threading.Lock()
threads = []

# Start Threads
for i in range(numThreads):
    name = "Thread-" + str(i)
    thread = downloadingThread(i, name, maxCount)
    thread.start()
    threads.append(thread)

# Finish Threads
for t in threads:
    t.join()

print("...done!")

# REPORT
# Testing print array
print("Printing Report:")
print(report)

# TC1: Report contains no duplicates
for c in report:
    # check that c only appears once
    num = 0
    for i in report:
        if i == c:
            num += 1

    if num != 1:
        print("UH OH ", c, " seems to appear ", num, " amount of times")

# TC2: Report contains every integer from 0 to maxcount
for i in range(maxCount):
    if not i in report:
        print("Ooops ", i, " is not even here!!")

# Report min number
min = report[0]
for c in report:
    if c < min:
        min = c
print("The smallest number was", min)

# Report max number
max = report[0]
for c in report:
    if c > max:
        max = c
print("The largest number was", max)

stop = timeit.default_timer()
print('Time: ', stop - start)
