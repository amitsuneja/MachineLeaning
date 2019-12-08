from oci.config import from_file
import oci
from oci.object_storage.models import CreateBucketDetails


# this is to configure the oci configuration file
my_config = from_file(file_location="C:\\Users\\amits\\Desktop\\Oracle_Cloud\\config_file_oci.txt")
print(my_config)
compartment_id = my_config['tenancy']
print(compartment_id)

"""
Create object storage client and get its namespace
"""
object_storage_client = oci.object_storage.ObjectStorageClient(my_config)
namespace = object_storage_client.get_namespace().data
namespace = namespace +"(root)/my_compartment"
print(namespace)

"""
define bucket_name and object_name variables
"""
bucket_name = "python-sdk-example-bucket"
object_name = "python-sdk-example-object"

"""
creating a bucket
"""
print("Creating a new bucket {!r} in compartment {!r}".format(bucket_name, compartment_id))
request = CreateBucketDetails()
request.compartment_id = compartment_id
request.name = bucket_name
bucket = object_storage_client.create_bucket(namespace, request)