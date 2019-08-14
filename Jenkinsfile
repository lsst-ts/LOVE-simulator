pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    imageName = "inriachile/love-simulator:${GIT_BRANCH}"
    atdomeImageName = "inriachile/love-atdome-sim:${GIT_BRANCH}"
    scriptqueueImageName = "inriachile/love-scriptqueue-sim:${GIT_BRANCH}"
    image = ""
    atdomeimage = ""
    scriptqueueImage = ""
    testCSCImage = ""
  }

  stages {
    stage("Build Simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/**/*"
          changeset "config/*"
          changeset "Dockerfile"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          image = docker.build(imageName, ".")
        }
      }
    }
    stage("Push Simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/**/*"
          changeset "config/*"
          changeset "Dockerfile"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            image.push()
          }
        }
      }
    }

    stage("Build ATDome simulator Docker image") {
      when {
        anyOf {
          changeset "csc-sim/atdome-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atdome"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          atdomeImage = docker.build(atdomeImageName, "-f ./Dockerfile-atdome .")
        }
      }
    }
    stage("Push ATDome simulator Docker image") {
      when {
        anyOf {
          changeset "csc-sim/atdome-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atdome"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            atdomeImage.push()
          }
        }
      }
    }

    stage("Build TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc-sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-testcsc"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          testCSCImage = docker.build(atdomeImageName, "-f ./Dockerfile-testcsc .")
        }
      }
    }
    stage("Push TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc-sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-testcsc"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            testCSCImage.push()
          }
        }
      }
    }

    stage("Build ScriptQueue simulator Docker image") {
      when {
        anyOf {
          changeset "csc-sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          scriptqueueImage = docker.build(scriptqueueImageName, "-f ./Dockerfile-scriptqueue .")
        }
      }
    }
    stage("Push ScriptQueue simulator Docker image") {
      when {
        anyOf {
          changeset "csc-sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
        }
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            scriptqueueImage.push()
          }
        }
      }
    }

    stage("Trigger develop deployment") {
      when {
        branch "develop"
      }
      steps {
        build(job: '../LOVE-integration-tools/develop', wait: false)
      }
    }
    stage("Trigger master deployment") {
      when {
        branch "master"
      }
      steps {
        build(job: '../LOVE-integration-tools/master', wait: false)
      }
    }
  }
}
