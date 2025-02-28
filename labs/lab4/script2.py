#!/usr/bin/env python3

import requests
import os
import boto3

s3=boto3.client('s3', region_name="us-east-1")

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded to {file_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")

# Example usage:
image_url = "https://www.icegif.com/wp-content/uploads/2022/10/icegif-760.gif"
file = "downloaded_image.gif"
path = os.path.join(os.getcwd(), file) # Saves to current directory

download_file(image_url, path)

bucket = 'ds2002-zmx3ra'
local_file = 'downloaded_image.gif'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file
)


import logging
import boto3
from botocore.exceptions import ClientError

bucket_name='ds2002-zmx3ra'
object_name='downloaded_image.gif'
expires_in=3600


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expires_in)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


# source used: https://stackoverflow.com/questions/39272744/when-to-use-a-boto3-client-and-when-to-use-a-boto3-resource
