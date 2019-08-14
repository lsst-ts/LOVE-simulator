pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    imageName = "inriachile/love-simulator:"
    atdomeImageName = "inriachile/love-atdome-sim:"
    scriptqueueImageName = "inriachile/love-scriptqueue-sim:"
    testCSCImageName = "inriachile/love-testcsc-sim:"
    image = ""
    atdomeImage = ""
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
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release") {
              image_tag = git_tag
            }
          }
          imageName = imageName + image_tag
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
          branch "release/*"
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
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release") {
              image_tag = git_tag
            }
          }
          atdomeImageName = atdomeImageName + image_tag
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
          branch "release/*"
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
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release") {
              image_tag = git_tag
            }
          }
          testCSCImageName = testCSCImageName + image_tag
          testCSCImage = docker.build(testCSCImageName, "-f ./Dockerfile-testcsc .")
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
          branch "release/*"
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
          branch "release/*"
        }
      }
      steps {
        script {
          def git_branch = "${GIT_BRANCH}"
          def image_tag = git_branch
          def slashPosition = git_branch.indexOf('/')
          if (slashPosition > 0) {
            git_tag = git_branch.substring(slashPosition + 1, git_branch.length())
            git_branch = git_branch.substring(0, slashPosition)
            if (git_branch == "release") {
              image_tag = git_tag
            }
          }
          scriptqueueImageName = scriptqueueImageName + image_tag
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
          branch "release/*"
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
