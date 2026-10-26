import numpy as np

speeds = np.array([
    [112, 90, 87, 87, 87], #monday
    [112, 87, 88, 75, 75], #tuesday
    [90, 82, 81, 75, 65], #wednesday
    [92, 87, 81, 71, 75], #thursday
    [100, 45, 40, 42, 45], #friday
])

print("Mean speed of each day", np.mean(speeds,axis=1))
print("Standard Deviation of each day", np.std(speeds,axis=1))
