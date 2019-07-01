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
  }

  stages {
    stage("Build Simulator Docker image") {
      when {
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          image = docker.build(imageName, "./")
        }
      }
    }
    stage("Push Simulator Docker image") {
      when {
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

  stages {
    stage("Build ATDome simulator Docker image") {
      when {
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          atdomeImage = docker.build(atdomeImageName, "./")
        }
      }
    }
    stage("Push ATDome simulator Docker image") {
      when {
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

  stages {
    stage("Build ScriptQueue simulator Docker image") {
      when {
        anyOf {
          branch "master"
          branch "develop"
        }
      }
      steps {
        script {
          scriptqueueImage = docker.build(scriptqueueImageName, "./")
        }
      }
    }
    stage("Push ScriptQueue simulator Docker image") {
      when {
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
