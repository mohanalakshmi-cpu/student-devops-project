
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
                sh 'python3 --version'
                sh 'python3 -m pip --version'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest -v test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-devops-project .'
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
