pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'python3 app.py'
            }
        }
        stage('Security Scan') {
            steps {
                echo 'Instalando herramientas de seguridad...'
                sh '''
                    python3 -m pip install --user bandit
                    echo "Ejecutando análisis estático con Bandit..."
                    python3 -m bandit -r . -f txt || true
                '''
            }
        }
    }
}
