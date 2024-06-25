import boto3
import botocore

# Initialize a Boto3 session with AWS credentials and region
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
region_name = 'your_region_name'

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)

# Function to read content from an S3 object
def read_from_s3(bucket_name, object_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        content = response['Body'].read().decode('utf-8')
        return content
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "NoSuchKey":
            print(f"The object with key '{object_key}' does not exist.")
        else:
            print(f"Error reading object '{object_key}' from bucket '{bucket_name}': {e}")

# Function to write content to an S3 object
def write_to_s3(bucket_name, object_key, data):
    try:
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=data.encode('utf-8'))
        print(f"Successfully wrote to s3://{bucket_name}/{object_key}")
    except botocore.exceptions.ClientError as e:
        print(f"Error writing object '{object_key}' to bucket '{bucket_name}': {e}")

# Example usage:
if __name__ == "__main__":
    bucket_name = 'S3_Bucket'
    object_key = 's3_bucket.txt'
    
    # Write to S3
    data_to_write = "Hello, this is a text written to S3."
    write_to_s3(bucket_name, object_key, data_to_write)
    
    # Read from S3
    retrieved_data = read_from_s3(bucket_name, object_key)
    if retrieved_data:
        print(f"Retrieved data from S3: {retrieved_data}")
