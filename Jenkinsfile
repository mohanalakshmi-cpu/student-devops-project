

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is available in the workspace'
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker --version'
                bat 'docker build -t student-management .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
