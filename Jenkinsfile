pipeline {
    agent any

    environment {
        GITHUB_CONTEXT = 'jenkins/build'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sinhaanshu/sonarqube-integration-jenkins.git'
                // Notify GitHub that the build has started
                githubNotify context: "${GITHUB_CONTEXT}", status: 'PENDING', description: 'Build started'
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
        success {
            echo "🎉 SonarQube Quality Gate passed!"
            githubNotify context: "${GITHUB_CONTEXT}", status: 'SUCCESS', description: 'Build and analysis passed'
        }

        failure {
            echo "❌ Pipeline failed due to Quality Gate or build issues."
            githubNotify context: "${GITHUB_CONTEXT}", status: 'FAILURE', description: 'Build or analysis failed'
        }

        always {
            echo "✅ Pipeline completed."
        }
    }
}
