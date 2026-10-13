
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t playwright-tests .'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                sh 'docker run --rm playwright-tests'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
