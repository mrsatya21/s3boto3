### Step 1 :

- Create an ***Instance profile role***, with **`AmazonS3FullAccess`** policy attached to it. 

- Launch an EC2 instance (*preferably* ***AL2023***, as all the steps are tested on AL2023 only) with the *Instance profile role* attached to it created previously and with user-data mentioned below :

- User data to install ***boto3*** in Ec2 instance : 

    > ```sh
    > #!/bin/bash -xe
    > 
    > sleep 60 
    > 
    > # Check python3 version (as AL2023 comes with python 3 preinstalled) :
    > python3 --version
    > 
    > # Install pip (Reference Link : https://pip.pypa.io/en/stable/installation/#get-pip-py) : 
    > wget https://bootstrap.pypa.io/get-pip.py
    > python3 get-pip.py
    > 
    > # Check AWS CLI version (as AL2023 comes with AWS CLI preinstalled) :
    > aws --version
    > 
    > # Install boto3 (Reference Link : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#using-the-aws-common-runtime-crt) : 
    > pip -q install boto3
    > ```

### Step 2: 

- Set the bucket name for which you have to list objects (*replace <BUCKET_NAME> with the real one as per your use case*) : 

    > ```sh
    > # Get Bucket name :
    > BUCKET_NAME=<BUCKET_NAME>
    > ```

### Step 3 : 

#### Option 1: 
- Create a file with extension *py* say **`getobjects.py`** and put all the codes here : 

    > ```sh
    > cat << EOF > getobjects.py
    > import boto3
    > 
    > def list_files_in_s3_bucket(bucket_name):
    >     # Initialize a session using Amazon S3
    >     client = boto3.client('s3')
    > 
    >     # Initialize the paginator for list_objects_v2
    >     paginator = client.get_paginator('list_objects_v2')
    >     
    >     # Create a PageIterator from the paginator
    >     page_iterator = paginator.paginate(Bucket=bucket_name)
    > 
    >     # Iterate through each page returned by the paginator
    >     for page in page_iterator:
    >         if 'Contents' in page:
    >             for obj in page['Contents']:
    >                 print(obj['Key'])
    > 
    > if __name__ == "__main__":
    >     # Specify your S3 bucket name
    >     bucket_name = '$BUCKET_NAME'
    >     
    >     # Call the function to list files
    >     list_files_in_s3_bucket(bucket_name)
    > EOF
    > ```

#### Option 2: 
- Run the command : 

    > ```sh
    > wget https://raw.githubusercontent.com/mrsatya21/s3boto3/main/getobjects.py
    > ```

### Step 4 : 

- Get the output : 

    > ```sh
    > # Get the S3 bucket list using the below command : 
    > python3 getobjects.py
    > ```
