pipeline {
    agent { docker { image 'python:3.9-slim' } } 
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
                sh 'pip install bandit'
                echo 'Ejecutando análisis estático con Bandit...'
                sh 'bandit -r . || true' 
            }
        }
    }
}
