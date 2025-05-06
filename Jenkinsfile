pipeline {
    agent {
        docker {
            image 'tiangolo/uvicorn-gunicorn-fastapi:python3.10'
            args '-u root:root'
        }
    }

    environment {
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                echo '🔧 Installation des dépendances Python...'
                sh '''
                    pip install --upgrade pip
                    pip install numpy==1.24.4
                    pip install -r requirements.txt
                    python -m spacy download en_core_web_sm
                '''
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Lancement des tests unitaires...'
                sh 'pytest tests'
            }
        }

        stage('Docker Build') {
            steps {
                echo '🐳 Build de l\'image Docker...'
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
            echo '🧹 Nettoyage des fichiers temporaires...'
            // Exécuter le nettoyage uniquement si Docker est installé
            sh 'command -v docker >/dev/null 2>&1 && docker system prune -af --volumes || echo "Docker non trouvé, nettoyage ignoré."'
        }
        failure {
            echo '❌ Une erreur est survenue dans la pipeline.'
        }
        success {
            echo '✅ Pipeline terminée avec succès !'
        }
    }
}
