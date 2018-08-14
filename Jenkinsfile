pipeline {
  agent none
  stages {
    stage('Build') {
      agent {
        dockerfile {
          filename 'Dockerfile'
          additionalBuildArgs '--tag helper_python_package'
        }

      }
      steps {
        echo 'Build Finished'
      }
    }
    stage('Test') {
      agent {
        docker {
          image 'helper_python_package:latest'
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
        sh 'cd "$PROJECT_PATH/" && ./static_check.sh'
      }
    }
  }
}