pipeline{
    agent{
        label "x201"
    }
    triggers {
        githubPush()
    }
    stages{
        stage("Unit Tests"){
            steps{
                echo "========executing Unit Tests========"
                sh "python test_calculator.py"
            }
        }
    }
    post{
        always{
            echo "========always========"
            echo "Notification sent to devops team"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}