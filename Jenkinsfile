// Jenkinsfile - Pipeline DevSecOps Completo 
pipeline { 
    agent any 
 
    stages { 
        stage('Build') { 
            steps { 
                echo 'Construyendo el proyecto...' 
            } 
        } 
 
        stage('Test') { 
            steps { 
                echo 'Ejecutando pruebas...' 
            } 
        } 
 
        stage('Security Scan') { 
            steps { 
                echo 'Instalando herramientas de seguridad...' 
                echo 'Ejecutando analisis estatico con Bandit...' 
            } 
        } 
    } 
 
    post { 
        always { 
            echo 'Pipeline DevSecOps completado' 
        } 
    } 
} 
