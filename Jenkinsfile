pipeline {
    agent any

    environment {
        IMAGE_NAME = 'text-analyzer-api'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Récupération du code source...'
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                echo '🔧 Installation des dépendances...'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'python -m spacy download en_core_web_sm'
            }
        }

        stage('Tests') {
            steps {
                echo '🧪 Exécution des tests...'
                sh 'pytest tests'
            }
        }

        stage('Docker Build') {
            steps {
                echo '🐳 Construction de l’image Docker...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Docker Run') {
            steps {
                echo '🚀 Lancement du conteneur...'
                sh "docker run -d -p 8000:80 --name ${IMAGE_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            echo '🧹 Nettoyage...'
            sh "docker rm -f ${IMAGE_NAME} || true"
            sh "docker system prune -af --volumes || true"
        }
        failure {
            echo '❌ Échec de la pipeline.'
        }
        success {
            echo '✅ Pipeline exécutée avec succès.'
        }
    }
}
