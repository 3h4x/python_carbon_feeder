
import sys
import socket
import time

key = sys.argv[1]

last_timestamp = int(time.time())
count = 1

line = sys.stdin.readline()
while line:
        timestamp = int(time.time())
        line = sys.stdin.readline()
        if last_timestamp == timestamp:
                count +=1
        else:
                code = line.split(" ")[1]
                print("{}.{}.{} {} {}".format(socket.gethostname(), key, code, count, last_timestamp))
                count = 1
                last_timestamp = timestamp
