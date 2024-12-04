pipeline {
    agent any

    environment {
        S3_BUCKET = 'varun-sam-artifacts-bucket' // S3 bucket name
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/your-repo-name.git' // GitHub repo URL
            }
        }

        stage('Build SAM Application') {
            steps {
                sh 'sam build'
            }
        }

        stage('Package Application') {
            steps {
                sh """
                sam package \
                    --s3-bucket ${S3_BUCKET} \
                    --output-template-file packaged.yaml
                """
            }
        }

        stage('Deploy Application') {
            steps {
                sh """
                sam deploy \
                    --template-file packaged.yaml \
                    --stack-name varun-lambda-api-stack \ // stack name
                    --capabilities CAPABILITY_IAM
                """
            }
        }
    }
}
