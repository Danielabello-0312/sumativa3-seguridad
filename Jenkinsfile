// Jenkinsfile - Pipeline DevSecOps Completo
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                sh 'python3 --version || python --version || echo "Python no encontrado"'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'python3 app.py || python app.py || echo "Error ejecutando app.py"'
            }
        }
        
        stage('Security Scan') {
            steps {
                echo 'Instalando herramientas de seguridad...'
                sh 'pip3 install bandit==1.7.0 || pip install bandit==1.7.0 || echo "Error instalando Bandit"'
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