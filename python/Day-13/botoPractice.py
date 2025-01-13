import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='mahendra834-python-bucket1',
    )


print(response)