import os.path
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3
)
from constructs import Construct
from aws_cdk.aws_s3_assets import Asset

dirname = os.path.dirname(__file__)

class S3BucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Creating a bucket
        bucket = s3.Bucket(self, "S3Bucket", encryption=s3.BucketEncryption.S3_MANAGED, versioned=True)

        # # Creating a bucket policy object
        # bucket_policy = s3.BucketPolicy(self, "S3BucketPolicy", bucket=bucket)

        # # Adding the bucket policy statement to deny object and object version deletion
        # bucket_policy.document.add_statements(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.DENY,
        #         principals=[iam.AnyPrincipal()],
        #         actions=["s3:DeleteObject", "s3:DeleteObjectVersion"],
        #         resources=[f"${bucket.bucket_arn}/*"]
        #     )
        # )

