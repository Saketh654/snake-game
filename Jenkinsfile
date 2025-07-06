pipeline{
    agent any

    stages{
        stage('Clone') {
            steps {
                git 'https://github.com/Saketh654/snake-game.git'
            }
        }

        stage('Install Dependencies'){
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test'){
            steps{
                sh 'pytest'
            }
        }

        stage('Docker Build'){
            steps{
                sh 'docker build -t snakegame .'
            }
        }

        stage('Docker Run'){
            steps{
                sh 'docker run --rm snakegame || true'
            }
        }

        stage('Archive'){
            steps {
                archiveArtifacts artifacts: '**/*.py'
            }
        }
    }
}