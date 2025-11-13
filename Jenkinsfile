pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sinhaanshu/sonarqube-integration-jenkins.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube-25-04') {
                    script {
                        def scannerHome = tool 'sonar-scanner'
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=python-sonar-demo \
                            -Dsonar.projectName=python-sonar-demo \
                            -Dsonar.projectVersion=1.0 \
                            -Dsonar.sources=. \
                            -Dsonar.exclusions=**/__pycache__/**,**/tests/** \
                            -Dsonar.python.version=3.10 \
                            -Dsonar.sourceEncoding=UTF-8 \
                            -Dsonar.host.url=$SONAR_HOST_URL \
                            -Dsonar.login=$SONAR_AUTH_TOKEN
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            echo "✅ Pipeline completed."
        }
        success {
            echo "🎉 SonarQube Quality Gate passed!"
        }
        failure {
            echo "❌ Pipeline failed due to Quality Gate or build issues."
        }
    }
}
