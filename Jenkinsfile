pipeline {
  agent none
  stages {
    stage('Build') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        sh 'pwd'
        sh 'ls'
        echo '"hello"'
        sh 'cd /run/helper_python/'
      }
    }
    stage('Tests') {
      agent {
        docker {
          image '11c089ccc057eed56162f36d8dc89fff4895861f:latest'
        }

      }
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'cd /run/helper_python/; ls'
        sh '/run/helper_python/code_style.sh'
      }
    }
    stage('Local') {
      agent any
      steps {
        sh 'pwd'
        sh 'ls'
      }
    }
  }
}