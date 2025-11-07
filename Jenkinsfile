pipeline {
    agent any

    parameters {
        string(name: 'WIDTH', defaultValue: '1280', description: 'Screen width')
        string(name: 'HEIGHT', defaultValue: '720', description: 'Screen height')
    }

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

        stage('Run Test with Parameters') {
            steps {
                bat "\"C:\\Users\\nveerlax\\python.exe\" display_test.py ${params.WIDTH} ${params.HEIGHT}"
            }
        }
    }
}


