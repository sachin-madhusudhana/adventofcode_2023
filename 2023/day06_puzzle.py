import linecache

import numpy as np
import time

start_time = time.time()

# Part 1 && Part 3
# Edit the txt file manually 
line_time = linecache.getline(r"day06.txt", 1)
times = line_time.split(':')[1]

line_dist = linecache.getline(r"day06.txt", 2)
dist = line_dist.split(':')[1]

time_list = [int(num) for num in times.split()]
dist_list = [int(num) for num in dist.split()]

win = 1
for j, time_val in enumerate(time_list):
    """ val = 0
    if (time_val % 2 == 0):
        midpoint = time_val / 2
    else:
        midpoint = (time_val - 1) / 2

    #print(int(midpoint))
    for t in range(1,int(midpoint)):
        if ((time_val - t) * t) > dist_list[j]: # Quadratic equation
            val = t
            break

    if (time_val % 2 == 0):
        nbr_of_ways = ((int(midpoint) - val) * 2)  + 1
    else:
        nbr_of_ways = ((int(midpoint) - val) + 1) * 2 """
    
    # Method 2 based on quadratic equation from line 29

    root1 = np.floor((time_val - np.sqrt(time_val*time_val - (4*dist_list[j])))/2)
    root2 = np.floor((time_val + np.sqrt(time_val*time_val - (4*dist_list[j])))/2)
    nbr_of_ways = int(root2 - root1)

    win *= nbr_of_ways


print("Winning", win)
print("--- %s seconds ---" % (time.time() - start_time))

