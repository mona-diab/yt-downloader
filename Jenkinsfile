pipeline {
    agent any
  stage('Checkout Code') {
    steps {
        git branch: 'main', url: 'https://github.com/mona-diab/yt-downloader.git'
    }
}
  stage('Build Docker Image') {
    steps {
        script {
            sh "docker build -t youtube-downloader ."
        }
    }
}
  stage('Run Unit Tests') {
    steps {
        script {
            sh "pip install pytest"
            sh "pytest tests/"
        }
    }
}
stage('Push to Docker Hub') {
    steps {
        script {
            sh "docker tag youtube-downloader mona248/yt-downloader:latest"
            withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_HUB_PASS')]) {
                sh "echo $DOCKER_HUB_PASS | docker login -u mona248 --password-stdin"
                sh "docker push mona248/yt-downloader:latest"
            }
        }
    }
}
stage('Deploy Container') {
    steps {
        script {
            sh "docker stop nice_hodgkin || true"
            sh "docker rm nice_hodgkin || true"
            sh "docker run -d --name nice_hodgkin -p 8080:8080 mona248/yt-downloader:latest"
        }
    }
}
post {
    success {
        echo "✅ Deployment successful!"
        mail to: 'monadiab283@gmail.com',
             subject: "Jenkins Build Successful",
             body: "The build and deployment were successful!"
    }
    failure {
        echo "❌ Deployment failed!"
        mail to: 'monadiab283@gmail.com',
             subject: "Jenkins Build Failed",
             body: "The build or deployment failed. Please check Jenkins logs."
    }
}

