import numpy as np
import statistics

from collections import Counter

theFile = open("rent.txt", "r")
theInts = []
for val in theFile.read().split():
    theInts.append(int(val))
theFile.close()

theInts.sort

mean = np.mean(theInts)
print("Mean : ",mean)

median = np.median(theInts)
print("Median : ",median)

mode_value = statistics.mode(theInts)
print("Mode : ",mode_value)

data = Counter(theInts)

print("Frequency Table",data.most_common())

length = len(theInts)

quarter_index = int(0.25*length)
print("25th percentile : ",theInts[quarter_index])

half_index = int(0.5*length)
print("50th percentile : ",theInts[half_index])


lastquarter_index = int(0.75*length)
print("75th percentile : ",theInts[lastquarter_index])

print("Variance : ",np.var(theInts))

std_deviation = np.std(theInts)

co_variance = (std_deviation/mean)*100

print("Coefficent of Variance : ",co_variance)