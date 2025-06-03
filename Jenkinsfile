pipeline{
  agent any
  parameters {
        string(name: 'ENV', defaultValue: 'dev', description: 'Environment to deploy to')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests?')
        choice(name: 'REGION', choices: ['us-east-1', 'us-west-1', 'eu-central-1'], description: 'Choose AWS Region')
        password(name: 'SECRET_KEY', defaultValue: '', description: 'Sensitive key (masked)')
  }

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
            '''
          }
       }
    }
    stage ("Code Coverage"){
        steps{
        script{
            bat '''
              coverage report --fail-under=80
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