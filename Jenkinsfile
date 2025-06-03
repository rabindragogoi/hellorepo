pipeline{
  agent any

  stages {
    stage ("first Stage"){
       steps {
          script{
              echo "Hello first script Pipeline"
          }
       }
    }
    stage ("Build Stage"){
       steps {
          script{
            bat 'echo Hello from Windows CMD'
                bat '''
                    echo Multi-line block
                    dir
                '''
          }
       }
    }
  }
  post {
        always {
            echo 'This will always run after the pipeline execution.'  // Run after the pipeline completes
        }
        success {
            echo 'This will run only if the pipeline completes successfully.'
        }
        failure {
            echo 'This will run if the pipeline fails.'
        }
    }

}