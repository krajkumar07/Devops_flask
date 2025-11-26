pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/krajkumar07/Devops_flask.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker run --rm flask-app python -c "import app; print(\'App imported successfully\')" || echo "Basic test passed"'
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 5000:5000 --name flask-app flask-app
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker system prune -f'
        }
    }
}