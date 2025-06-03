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
    stage('Clone Repo') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/develop']],
                    userRemoteConfigs: [[
                        url: 'git@github.com:rabindragogoi/hellorepo.git',
                        credentialsId: 'github-credentials'
                    ]]
                ])
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