pipeline {
  agent { docker { image 'python:3.8-alpine' } }
  stages {
    stage('build') {
      steps {
        sh  'virtualenv .venv'
        sh 'source .venv/bin/activate'
        sh 'pip install -r requirements.txt'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}