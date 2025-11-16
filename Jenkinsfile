pipeline {
    agent any //any agent bwill take all labels
  
  environment {
    AWS_REGION  = 'ca-central-1'
    AWS_ACCOUNT = '975050024946'

    FRONTEND_REPO = 'vignesh-sample-mern-with-microservices-frontend'
    BACKEND_REPO  = 'vignesh-sample-mern-with-microservices-backend'

    AWS_CREDS_ID = 'aws-creds-vignesh'  // Jenkins credentials ID you created
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Set AWS Env Vars') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: AWS_CREDS_ID,
          usernameVariable: 'AWS_ACCESS_KEY_ID',
          passwordVariable: 'AWS_SECRET_ACCESS_KEY'
        )]) {
          sh '''
            echo "Checking STS identity..."
        aws sts get-caller-identity --region ${AWS_REGION}
          '''
        }
      }
    }

 stage('Login to ECR') {
  steps {
    sh '''
      aws ecr get-login-password --region ${AWS_REGION} \
      | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com
    '''
  }
}


    stage('Build & Push Backend') {
      steps {
        dir('backend') {
          script {
            def image = "${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${BACKEND_REPO}:latest"

            sh """
              echo 'Building backend image...'
              docker build -t ${BACKEND_REPO}:latest .
              docker tag ${BACKEND_REPO}:latest ${image}
              docker push ${image}
            """
          }
        }
      }
    }

    stage('Build & Push Frontend') {
      steps {
        dir('frontend') {
          script {
            def image = "${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${FRONTEND_REPO}:latest"

            sh """
              echo 'Building frontend image...'
              docker build -t ${FRONTEND_REPO}:latest .
              docker tag ${FRONTEND_REPO}:latest ${image}
              docker push ${image}
            """
          }
        }
      }
    }
  }

  post {
    always {
      script {
        sh "docker logout ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com || true"
      }
    }
  }
}
