import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Option A: Use default credentials chain
try:
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("S3 Buckets:")
    for b in response.get('Buckets', []):
        print(" -", b['Name'])
except (NoCredentialsError, PartialCredentialsError):
    print("No AWS credentials found. Configure them with 'aws configure' or set environment variables.")
except Exception as e:
    print("Error calling AWS:", e)
