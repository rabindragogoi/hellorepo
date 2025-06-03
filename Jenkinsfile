pipeline{
  agent any

  stages {
    stage ("Code Checkout"){
       steps {
          script{
             bat '''
                echo Multi-line block
                dir
             '''
          }
       }
    }
    stage ("Unittest"){
       steps {
          script{
            bat '''
            pytest --cov=app --cov-report=xml --cov-report=term --junitxml=tests\\results.xml
            coverage report --fail-under=90
            if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%
            '''
          }
       }
    }
    stage('Publish Results') {
        steps {
            junit 'tests\\results.xml'

            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'coverage.xml',
                reportName: 'Coverage Report'
            ])
        }
        }

  }
  post {
        always {
            echo 'This will always run after the pipeline execution.'  // Run after the pipeline completes
            deleteDir()
        }
        success {
            echo 'This will run only if the pipeline completes successfully.'
        }
        failure {
            echo 'This will run if the pipeline fails.'
        }
    }

}