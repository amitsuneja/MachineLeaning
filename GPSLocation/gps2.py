# Load packages
from pygeocoder import Geocoder
import pandas as pd
import numpy as np

# Create a dictionary of raw data
data = {'Site 1': '31.336968, -109.560959',
        'Site 2': '31.347745, -108.229963',
        'Site 3': '32.277621, -107.734724',
        'Site 4': '31.655494, -106.420484',
        'Site 5': '30.295053, -104.014528'}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame.from_dict(data, orient='index')

lat = []
lon = []

# For each row in a varible,
for row in df[0]:
    # Try to,
    try:
        # Split the row by comma, convert to float, and append
        # everything before the comma to lat
        lat.append(float(row.split(',')[0]))
        # Split the row by comma, convert to float, and append
        # everything after the comma to lon
        lon.append(float(row.split(',')[1]))
    # But if you get an error
    except:
        # append a missing value to lat
        lat.append(np.NaN)
        # append a missing value to lon
        lon.append(np.NaN)

# Create two new columns from lat and lon
df['latitude'] = lat
df['longitude'] = lon
print(df)

# Python3 program for reverse geocoding.


import reverse_geocoder as rg
import pprint


def reverseGeocode(coordinates):
    result = rg.search(coordinates)

    # result is a list containing ordered dictionary.
    pprint.pprint(result)


# Driver function
if __name__ == "__main__":
    # Coorinates tuple.Can contain more than one pair.
    coordinates = (28.613939, 77.209023)

    reverseGeocode(coordinates)