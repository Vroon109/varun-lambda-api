# Lambda API with Automated Deployment

This repository contains the code and scripts to:
- Create a Lambda function integrated with API Gateway.
- Define a deployment pipeline using Jenkins.
## Steps to Deploy
1. Use the `template.yaml` with AWS SAM CLI.
2. Use the `Jenkinsfile` to automate deployments.

## Folder Structure
- `app.py`: Lambda function code.
- `template.yaml`: AWS SAM template.
- `appspec.yml`: Deployment instructions for CodeDeploy.
- `scripts/`: Pre- and post-deployment hooks.
- `Jenkinsfile`: CI/CD pipeline configuration.


## Prerequisites
- AWS SAM CLI
- Python 3.9+
- Jenkins

