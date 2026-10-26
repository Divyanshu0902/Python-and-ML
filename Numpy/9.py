# basic statistics functionalities 

import numpy as np

speeds = np.array([112, 90, 87, 87, 87])

print("Speeds:", speeds)
print("max: ", np.max(speeds))
print("min: ", np.min(speeds))
print("sum: ", np.sum(speeds))
print("mean: ", np.mean(speeds))
print("standard deviation: ", np.std(speeds))
print("median: ", np.median(speeds))