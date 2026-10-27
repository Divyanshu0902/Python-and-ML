# mode calculation using counter 

import numpy as np
from collections import Counter

speeds = np.array([
    [112, 90, 87, 87, 87], #monday
    [112, 87, 88, 75, 75], #tuesday
    [90, 82, 81, 75, 65], #wednesday
    [92, 87, 81, 71, 75], #thursday
    [100, 45, 40, 42, 45], #friday
])

monday = speeds[0]
mode = Counter(monday).most_common(3)[0]

print("The most frequent speed of Monday is ",mode[0],", occuring",mode[1],"times.")
