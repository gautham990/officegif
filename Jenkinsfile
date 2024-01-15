pipeline {

    agent any
    parameters {
        string(name: 'RELEASE', description: 'Release version in major.minor.fix format')
        }
    options {
        timeout(10)   
        }
    stages {
        stage("Code Test") {
            steps {
                sh "echo Some test..."
            }    
        } 
        stage("Docker Build") {
            steps {
                sh "docker build -t officegif:latest ."
                sh "docker tag officegif gautham990/officegif:$RELEASE"
            }
        }  
        stage("Docker Push") {
            steps {
                withDockerRegistry([ credentialsId: "gautha990-dockerhub", url: "" ]) {
                    sh  "docker push gautham990/officegif:$RELEASE"
                }
            }
        }
        stage("Run Docker and cleanup") {
            steps {
                sh "docker run --name officegif -d -p 5000:5000 gautham990/officegif:$RELEASE"
                sh "sleep 120"
                sh "docker container rm officegif --force"
            }
        }
    }
}     


