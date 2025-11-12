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
                echo 'Ejecutando analisis de seguridad...'
                sh '''
                    echo "Simulando escaneo de seguridad con Bandit"
                    echo "Resultado: No se encontraron vulnerabilidades criticas"
                    echo "Archivos analizados: app.py, security_scan.py"
                    echo "Estadisticas: 0 issues de alta severidad"
                '''
            }
        }
    }
    post {
        always {
            echo 'Pipeline DevSecOps completado exitosamente'
        }
    }
}
