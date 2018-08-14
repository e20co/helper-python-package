pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('LS') {
      steps {
        sh 'ls'
        sh 'pwd'
      }
    }
  }
}