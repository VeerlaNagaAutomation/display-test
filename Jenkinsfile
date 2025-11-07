pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VeerlaNagaAutomation/display-test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\nveerlax\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\nveerlax\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\nveerlax\\python.exe" display_test.py'
            }
        }
    }
}
