import boto3


class S3Service:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def scan_buckets(self, region: str):
        if region:
            self.s3 = boto3.client('s3', region_name=region)
        response = self.s3.list_buckets()
        return response
