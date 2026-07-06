pipeline {
    agent any

    stages {

        stage('Code Clone') {
            steps {
                sh 'whoami'
                git branch: 'main', url: 'https://github.com/shaikhirfan82/Flask-EMS-App.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t shaikhirfan82/flask-ems-app:latest .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u shaikhirfan82 --password-stdin
                    docker push shaikhirfan82/flask-ems-app:latest
                    '''
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