#!/usr/bin/python3
import sys
counts = []
for line in sys.stdin:
    age, count =line.split()
    counts.append(int(count))

print('Average Shares:', sum(counts)/len(counts))

