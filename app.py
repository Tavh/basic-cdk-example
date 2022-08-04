#!/usr/bin/env python3
import os

import aws_cdk as cdk

from basic_cdk_example.ec2_instance_stack import EC2InstanceStack
from basic_cdk_example.s3_bucket_stack import S3BucketStack


app = cdk.App()
EC2InstanceStack(app, "EC2InstanceStack")
S3BucketStack(app, "S3BucketStack")

app.synth()
