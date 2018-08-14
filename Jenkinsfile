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
        echo 'Build Finished'
      }
    }
    stage('Tests') {
      agent {
        docker {
          image '11c089ccc057eed56162f36d8dc89fff4895861f:latest'
        }

      }
      environment {
        PYTHONPATH = '/run/helper_python/'
        PROJECT_PATH = '/run/helper_python'
      }
      steps {
        sh '"$PROJECT_PATH/test.sh"'
        sh '"$PROJECT_PATH/code_style.sh"'
        sh '"$PROJECT_PATH/coverage.sh"'
        sh 'cd "$PROJECT_PATH/" && ls'
      }
    }
    stage('Local') {
      agent any
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'cd /run; ls'
      }
    }
  }
}