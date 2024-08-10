import boto3

def list_files_in_s3_bucket(bucket_name):
    # Initialize a session using Amazon S3
    client = boto3.client('s3')

    # Initialize the paginator for list_objects_v2
    paginator = client.get_paginator('list_objects_v2')
    
    # Create a PageIterator from the paginator
    page_iterator = paginator.paginate(Bucket=bucket_name)

    # Iterate through each page returned by the paginator
    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                print(obj['Key'])

if __name__ == "__main__":
    # Specify your S3 bucket name
    bucket_name = '$BUCKET_NAME'
    
    # Call the function to list files
    list_files_in_s3_bucket(bucket_name)