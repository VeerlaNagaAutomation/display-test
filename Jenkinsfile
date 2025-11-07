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

        stage('Run Tests Locally') {
            steps {
                bat '"C:\\Users\\nveerlax\\python.exe" -m pytest -v --html=report.html --self-contained-html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
