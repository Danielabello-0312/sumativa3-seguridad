pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  # Python 3.9 compatible con Bandit
            reuseNode true
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Danielabello-0312/sumativa3-seguridad.git'
            }
        }
        
        stage('Build') {
            steps {
                echo '🔨 Construyendo el proyecto...'
                sh 'python --version'
            }
        }
        
        stage('Security Scan') {
            steps {
                echo '🔍 Ejecutando análisis de seguridad...'
                sh 'python security_scan.py'
            }
        }
        
        stage('Deploy') {
            steps {
                echo '🚀 Desplegando aplicación...'
            }
        }
    }
    
    post {
        always {
            echo '🎉 Pipeline completado'
        }
    }
}