pipeline {
    agent any
    options {
        timeout(10)   
        }   
    stages {
        stage("Read release number") {
            steps {
                 script {
                    def props = readProperties file: 'release.properties' 
                    env.RELEASE = props.RELEASE
                }
            }
        }
        stage("Code Test") {
            steps {
                sh "echo Some test..."
                sh "sleep 50"
                sh "echo ${RELEASE}"
            }    
        } 
        stage("Docker Build") {
            steps {
                sh "docker build -t officegif:latest ."
                sh "docker tag officegif gautham990/officegif:${RELEASE}"
            }
        }  
        stage("Docker Push") {
            steps {
                withDockerRegistry([ credentialsId: "gautha990-dockerhub", url: "" ]) {
                    sh  "docker push gautham990/officegif:${RELEASE}"
                }
            }
        }
        stage("Run Docker and cleanup") {
            steps {
                sh "docker run --name officegif -d -p 5000:5000 gautham990/officegif:${RELEASE}"
                sh "sleep 120"
                sh "docker container rm officegif --force"
            }
        }
    }
}     


