pipeline {
    agent {
        docker {
            image 'tiangolo/uvicorn-gunicorn-fastapi:python3.10'
            args '-u root:root' // pour éviter les problèmes de permissions
        }
    }

    environment {
        PIP_NO_CACHE_DIR = 'false'
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PIP_ROOT_USER_ACTION = 'ignore'
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
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    python -m spacy download en_core_web_sm
                '''
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
                sh 'docker build -t text-analyzer-api .'
            }
        }

        stage('Docker Run') {
            steps {
                echo '🚀 Lancement du conteneur Docker...'
                sh 'docker run -d -p 8000:80 --name text-analyzer-api text-analyzer-api'
            }
        }
    }

    post {
        always {
            echo '🧹 Nettoyage...'
            sh 'docker system prune -af --volumes || true'
        }
        failure {
            echo '❌ Échec de la pipeline.'
        }
        success {
            echo '✅ Pipeline terminée avec succès.'
        }
    }
}
