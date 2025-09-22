pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Get code from GitHub
                git branch: 'main', url: 'https://github.com/VeerlaNagaAutomation/display-test.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Use your python.exe path
                bat '"C:\\Users\\nveerlax\\python.exe" --version'
            }
        }

        stage('Run Test') {
            steps {
                // Run your Python test file
                bat '"C:\\Users\\nveerlax\\python.exe" display_test.py'
            }
        }
    }
}
