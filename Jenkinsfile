pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t shaikhirfan82/flask-ems:latest .'
      }
    }
    stage('Push') {
      steps {
        withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u yourdockerhub --password-stdin'
          sh 'docker push yourdockerhub/flask-ems:latest'
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'kubectl apply -f k8s-deployment.yaml'
      }
    }
  }
}
