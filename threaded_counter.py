#! /usr/bin/python3

# KennyC 05.01.21
#
# USAGE:
# python3 threaded_counter.py [NUM_THREADS] [MAX_COUNT]


import threading
import timeit
import sys

start = timeit.default_timer()

# Globals
counter = 0
report = []

class countingThread(threading.Thread):
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
                print (self.name, "Finished")
                threadLock.release()
                break
            counter += 1

            threadLock.release()

            # Execute
            print (self.name, myCount)
            report.append(myCount)
        
# Get Command Line Arguments
numThreads = 2
maxCount = 100

if len(sys.argv) > 1:
    numThreads = int(sys.argv[1])
if len(sys.argv) > 2:
    maxCount = int(sys.argv[2])
    if maxCount > sys.maxsize:
        maxCount= sys.maxsize

print("Starting program with", numThreads, "threads, counting up to", maxCount, "...")

# Threads
threadLock = threading.Lock()
threads = []

# Start Threads
for i in range(numThreads):
    name = "Thread-" + str(i)
    thread = countingThread(i, name, maxCount)
    thread.start()
    threads.append(thread)

# Finish Threads
for t in threads:
    t.join()

print ("...done!")

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
    
    if num != 1 :
        print("UH OH ", c, " seems to appear ", num, " amount of times")

# TC2: Report contains every integer from 0 to maxcount
for i in range(maxCount):
    if not i in report:
        print("Ooops ", i , " is not even here!!")

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

# Print Time
stop = timeit.default_timer()
print('Time: ', stop - start)