pipeline {
  agent none
  stages {
    stage('Clone') {
      steps {
        git(url: 'https://github.com/e20co/helper-python-package.git', branch: 'master')
      }
    }
  }
}