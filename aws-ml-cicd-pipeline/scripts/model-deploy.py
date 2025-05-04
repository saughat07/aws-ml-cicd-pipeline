import boto3
import time

timestamp = int(time.time())
model_name = f"ml-model-{timestamp}"
endpoint_name = "ml-endpoint"

s3 = boto3.client("s3")
sm = boto3.client("sagemaker")

# Upload model artifact
s3.upload_file("model/model.joblib", "YOUR_S3_BUCKET", "model/model.joblib")

# Create model
response = sm.create_model(
    ModelName=model_name,
    PrimaryContainer={
        "Image": "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3",
        "ModelDataUrl": f"s3://YOUR_S3_BUCKET/model/model.joblib"
    },
    ExecutionRoleArn="YOUR_SAGEMAKER_EXEC_ROLE"
)

# Create endpoint config
sm.create_endpoint_config(
    EndpointConfigName=f"{endpoint_name}-config",
    ProductionVariants=[{
        "VariantName": "AllTraffic",
        "ModelName": model_name,
        "InitialInstanceCount": 1,
        "InstanceType": "ml.t2.medium"
    }]
)

# Create endpoint
sm.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=f"{endpoint_name}-config"
)
