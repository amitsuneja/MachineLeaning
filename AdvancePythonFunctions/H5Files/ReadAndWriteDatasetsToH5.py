import h5py as h5
import numpy as np

# Read H5 file
my_file = h5.File("test_catvnoncat.h5", "r")

# Get list of datasets name within the H5 file
datasets = (key for key in my_file.keys())
print(type(datasets))

# print list of datasets name within the H5 file
i = 0
dict_of_arrays = {}
for datasetname in datasets:
    print("dataset No {} named = {} and its shape={}".format(i, datasetname,my_file[datasetname].shape))
    dict_of_arrays[i] = np.array(my_file[datasetname][:])
    i = i + 1

print(dict_of_arrays[0].dtype)  # |S7
"""
The dtype object describes how the bytes in the fixed-size block of memory corresponding to an array item should be 
interpreted. It describes different aspects of the data such as:
1. Type of data
2. Size of the data
3. Byte order of the data etc.
The Byte Order (also known as endianness) describes the sequence or order of bytes. 
They are arranged to form larger values, which comes in handy when storing the file or sharing it. 
The Byte Order is important to be known since bytes (and bits) can be represented in two different ways, 
ordered from the most significant or the least significant one.

Big-endian: storage or sending starts with the byte containing the most significant bit with the 
significance decreasing
Little-endian: storage or sending starts with the byte containing the least significant bit with 
the significance increasing
The big-endian Byte Order is the more common one of the two. 
Mixed cases of the two exist as well (mixed-endian, middle-endian).

It may happen that files are created on a machine or computer that creates files using big-endian, for example.
These cannot be correctly interpreted by machines reading little-endian only. Thus, the Byte Order of a file 
provides information which way the file can be opened or processed.

Here, 'S7' means that the object is of type string and it's size(no. of bytes) is 7"""

print(dict_of_arrays[0].itemsize)  # 7
print(dict_of_arrays[1].dtype)     # uint8
print(dict_of_arrays[1].itemsize)  # 1
print(dict_of_arrays[2].dtype)     # int64
print(dict_of_arrays[2].itemsize)  # 8
print(dict_of_arrays[0])           # [b'non-cat' b'cat']
print(dict_of_arrays[1])
print(dict_of_arrays[2])

# Read H5 file

# Creating 2 datasets arrays
my_array_X = np.random.randn(1000).reshape(10,100)
my_array_Y = np.random.randn(1000)


with h5.File('random.h5', 'w') as my_file:
    dset = my_file.create_dataset("X_dataset", data=my_array_X, compression="gzip", compression_opts=9)
    dset = my_file.create_dataset("Y_dataset", data=my_array_Y, compression="gzip", compression_opts=9)


my_file = h5.File("random.h5", "r")
datasets = (key for key in my_file.keys())
# print list of datasets name within the H5 file
i = 0
dict_of_arrays = {}
for datasetname in datasets:
    print("dataset No {} named = {} and its shape={}".format(i, datasetname,my_file[datasetname].shape))
    dict_of_arrays[i] = np.array(my_file[datasetname][:])
    i = i + 1





