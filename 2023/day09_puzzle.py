import re
import numpy as np
data = open('day_09.txt', 'r').read().split('\n')

overall_history = []
old_history = []

for line in data:
    
    store_last = 0
    store_first = []
    converted_list = [int(item) for item in line.split()]

    store_first.append(converted_list[0])
    store_last += converted_list[-1]

    history = np.diff(converted_list)
    store_last += history[-1]
    store_first.append(history[0])

    while (any(history)):
        history = np.diff(history)
        store_last += history[-1]
        store_first.append(history[0])

    store_first.reverse()
    val = store_first[0]
    for i in range(len(store_first)-1):
        val = store_first[i+1] - val
    overall_history.append(store_last)
    old_history.append(val)

print("Part 1 : ", sum(overall_history))
print("Part 2 : ", sum(old_history))