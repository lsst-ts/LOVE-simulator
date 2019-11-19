pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    imageName = "lsstts/love-simulator:"
    atdomeImageName = "lsstts/love-atdome-sim:"
    atmcsImageName = "lsstts/love-atmcs-sim:"
    scriptqueueImageName = "lsstts/love-scriptqueue-sim:"
    watcherImageName = "lsstts/love-watcher-sim:"
    testCSCImageName = "lsstts/love-testcsc-sim:"
    image = ""
    atdomeImage = ""
    atmcsImage = ""
    scriptqueueImage = ""
    watcherImage = ""
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
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
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
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
          changeset "csc_sim/atdome-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atdome"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
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
          changeset "csc_sim/atdome-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atdome"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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

    stage("Build ATMCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atmcs-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atmcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          atmcsImageName = atmcsImageName + image_tag
          atmcsImage = docker.build(atmcsImageName, "-f ./Dockerfile-atmcs .")
        }
      }
    }
    stage("Push ATMCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atmcs-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-atmcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            atmcsImage.push()
          }
        }
      }
    }

    stage("Build TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-testcsc"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
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
          changeset "csc_sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-testcsc"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
          changeset "csc_sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
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
          changeset "csc_sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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

    stage("Build Watcher simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/watcher-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-watcher"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix") {
              image_tag = git_tag
            }
          }
          watcherImageName = watcherImageName + image_tag
          watcherImage = docker.build(watcherImageName, "-f ./Dockerfile-watcher .")
        }
      }
    }
    stage("Push Watcher simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/watcher-setup.sh"
          changeset "config/*"
          changeset "Dockerfile-watcher"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "master"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            watcherImage.push()
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
