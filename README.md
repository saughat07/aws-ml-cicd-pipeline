# aws-ml-cicd-pipeline
Terraform template to provision an AWS CodePipeline that automates the CI/CD workflow for training and deploying an ML model to Amazon SageMaker

Here’s a Terraform template to provision an AWS CodePipeline that automates the CI/CD workflow for training and deploying an ML model to Amazon SageMaker. This includes:

1. CodeCommit repository
2. CodeBuild project
3. S3 artifact bucket
4. SageMaker execution role
5. CodePipeline definition

Directory Structure

ml-cicd-pipeline/
├── main.tf
├── variables.tf
├── outputs.tf
├── buildspec.yml
└── scripts/
    ├── train.py
    └── model-deploy.py

Next Steps:-

1. Run terraform init
2. Run terraform apply
3. Clone the repo using output repository_url, push your ML code
4. CodePipeline will trigger, train your model, and deploy it using SageMaker

