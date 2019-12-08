# importing libraries
# from oci.config import validate_config

import os
import oci
import io
from oci.config import from_file

data_dir = "D:\\DataScienceAndStats\\artificialintelligence\\CS223A"
files_to_process = [file for file in os.listdir(data_dir) if file.endswith('txt')]
bucket_name = "Sales_Data"

# this is to configure the oci configuration file
my_config = from_file(file_location="C:\\Users\\amits\\Desktop\\Oracle_Cloud\\config_file_oci.txt")
print(my_config)

# Test Configuration file of oci
# print(validate_config(my_config))

"""
Create object storage client and get its namespace
"""
object_storage_client = oci.object_storage.ObjectStorageClient(my_config)
namespace = object_storage_client.get_namespace().data
print(namespace)
my_list = oci.identity.identity_client.IdentityClient.list_compartments
print(my_list)

for comp in my_list:
    print(comp)