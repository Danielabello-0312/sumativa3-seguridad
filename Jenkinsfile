pipeline {
    agent any
    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
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
                    python3 -m venv security_scan
                    . security_scan/bin/activate
                    pip install bandit==1.7.0
                    echo "Ejecutando analisis estatico con Bandit..."
                    bandit -r . -f txt -o bandit_report.txt
                    echo "=== RESULTADO DE BANDIT ==="
                    cat bandit_report.txt
                    echo "==========================="
                '''
            }
        }
    }
    post {
        always {
            echo 'Pipeline DevSecOps completado'
        }
    }
}
