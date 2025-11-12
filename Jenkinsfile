// Jenkinsfile - Pipeline DevSecOps Completo
pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                sh 'python --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'python app.py'
            }
        }

        stage('Security Scan') {
            steps {
                echo 'Instalando herramientas de seguridad...'
                sh 'pip install -r requirements.txt'
                echo 'Ejecutando analisis estatico con Bandit...'
                sh 'bandit -r . -f txt || true'
            }
        }
    }

    post {
        always {
            echo 'Pipeline DevSecOps completado'
        }
    }
}
