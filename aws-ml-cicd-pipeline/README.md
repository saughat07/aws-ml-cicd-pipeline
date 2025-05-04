# AWS ML CI/CD Pipeline

This repository provides a Terraform-based CI/CD pipeline using AWS CodePipeline, CodeBuild, and SageMaker for training and deploying ML models.

## Structure

- `scripts/train.py`: Trains a basic ML model.
- `scripts/model-deploy.py`: Deploys the trained model to SageMaker.
- `buildspec.yml`: CodeBuild configuration.
- `main.tf`: Terraform infrastructure setup.

## Usage

1. Update placeholders in `model-deploy.py`.
2. Run `terraform init && terraform apply`.
3. Push code to CodeCommit to trigger the pipeline.

