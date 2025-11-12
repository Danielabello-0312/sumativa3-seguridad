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
                    # Instalar Bandit
                    pip install --break-system-packages bandit==1.7.0
                    
                    # Encontrar la ruta exacta de bandit
                    BANDIT_PATH=$(which bandit)
                    echo "Bandit encontrado en: $BANDIT_PATH"
                    
                    # Ejecutar bandit con ruta absoluta
                    echo "Ejecutando analisis estatico con Bandit..."
                    $BANDIT_PATH -r . -f txt -o bandit_report.txt
                    
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
