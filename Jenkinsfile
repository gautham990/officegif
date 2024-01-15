pipeline {

    agent any
    parameters {
        string(name: 'RELEASE', description: 'Release version in major.minor.fix format')
    }

    options {
        timeout(10)     //Restrict the job to 10mins
        buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '3', numToKeepStr: '3') //Discard old builds
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
                withDockerRegistry([ credentialsId: "gautham990-dockerhub", url: "" ]) {
                    sh  "docker push gautham990/officegif:$RELEASE"
                }
            }
        }
        stage("Run Docker") {
            steps {
                sh "docker run -d -p 5000:80 gautham990/officegif:$RELEASE"
                }
        }
    }
}     


