# Read-and-Write-S3-bucket-using-Python
basic Python script that demonstrates reading from and writing to an Amazon S3 bucket using the boto3 library

# NOTE :
Installation: Make sure you have the boto3 library installed (pip install boto3).
AWS Credentials: Replace YOUR_ACCESS_KEY_ID, YOUR_SECRET_ACCESS_KEY, and YOUR_AWS_REGION with your actual AWS credentials and region.
Usage: Replace your-bucket-name with the name of your S3 bucket and adjust object_key accordingly.
Functions:
read_from_s3(bucket_name, object_key): Reads content from an object in the specified S3 bucket.
write_to_s3(bucket_name, object_key, data): Writes data to an object in the specified S3 bucket.
