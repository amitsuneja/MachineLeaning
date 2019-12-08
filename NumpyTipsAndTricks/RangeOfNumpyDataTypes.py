import numpy as np

int_types = ["uint8", "int8", "int16", "int32", "int64"]

for it in int_types:
    print(np.iinfo(it))