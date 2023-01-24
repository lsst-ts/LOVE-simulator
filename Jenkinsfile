pipeline {
  agent any
  environment {
    registryCredential = "dockerhub-inriachile"
    imageName = "lsstts/love-simulator:"
    atcsImageName = "lsstts/love-atcs-sim:"
    mtcsImageName = "lsstts/love-mtcs-sim:"
    scriptqueueImageName = "lsstts/love-scriptqueue-sim:"
    watcherImageName = "lsstts/love-watcher-sim:"
    weatherstationImageName = "lsstts/love-weatherstation-sim:"
    testCSCImageName = "lsstts/love-testcsc-sim:"
    jupyterImageName = "lsstts/love-jupyter:"
    image = ""
    atcsImage = ""
    mtcsImage = ""
    scriptqueueImage = ""
    watcherImage = ""
    weatherstationImage = ""
    testCSCImage = ""
    jupyterImage = ""
    user_ci = credentials('lsst-io')
    LTD_USERNAME="${user_ci_USR}"
    LTD_PASSWORD="${user_ci_PSW}"
  }

  stages {
    stage("Build ATCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atcs-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-atcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          atcsImageName = atcsImageName + image_tag
          atcsImage = docker.build(atcsImageName, "-f docker/Dockerfile-atcs .")
        }
      }
    }
    stage("Push ATCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/atcs-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-atcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            atcsImage.push()
          }
        }
      }
    }

    stage("Build MTCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/mtcs-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-mtcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          mtcsImageName = mtcsImageName + image_tag
          mtcsImage = docker.build(mtcsImageName, "-f docker/Dockerfile-mtcs .")
        }
      }
    }
    stage("Push MTCS simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/mtcs-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-mtcs"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            mtcsImage.push()
          }
        }
      }
    }

    stage("Build TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-testcsc"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          testCSCImageName = testCSCImageName + image_tag
          testCSCImage = docker.build(testCSCImageName, "-f docker/Dockerfile-testcsc .")
        }
      }
    }
    stage("Push TestCSC simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/testcsc-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-testcsc"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
          changeset "docker/Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          scriptqueueImageName = scriptqueueImageName + image_tag
          scriptqueueImage = docker.build(scriptqueueImageName, "-f docker/Dockerfile-scriptqueue .")
        }
      }
    }
    stage("Push ScriptQueue simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/scriptqueue-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-scriptqueue"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
          changeset "docker/Dockerfile-watcher"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          watcherImageName = watcherImageName + image_tag
          watcherImage = docker.build(watcherImageName, "-f docker/Dockerfile-watcher .")
        }
      }
    }

    stage("Push Watcher simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/watcher-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-watcher"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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

    stage("Build WeatherStation simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/weatherstation-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-weatherstation"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          weatherstationImageName = weatherstationImageName + image_tag
          weatherstationImage = docker.build(weatherstationImageName, "-f docker/Dockerfile-weatherstation .")
        }
      }
    }

    stage("Push WeatherStation simulator Docker image") {
      when {
        anyOf {
          changeset "csc_sim/weatherstation-setup.sh"
          changeset "config/*"
          changeset "docker/Dockerfile-weatherstation"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            weatherstationImage.push()
          }
        }
      }
    }
    stage("Build Jupyter simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/jupyter.sh"
          changeset "docker/Dockerfile-jupyter"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
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
            if (git_branch == "release" || git_branch == "hotfix" || git_branch == "bugfix" || git_branch == "tickets") {
              image_tag = git_tag
            }
          }
          jupyterImageName = jupyterImageName + image_tag
          jupyterImage = docker.build(jupyterImageName, "-f docker/Dockerfile-jupyter .")
        }
      }
    }
    stage("Push Jupyter simulator Docker image") {
      when {
        anyOf {
          changeset "simulator/jupyter.sh"
          changeset "docker/Dockerfile-jupyter"
          changeset "Jenkinsfile"
          expression {
            return currentBuild.number == 1
          }
        }
        anyOf {
          branch "main"
          branch "develop"
          branch "bugfix/*"
          branch "hotfix/*"
          branch "release/*"
          branch "tickets/*"
        }
      }
      steps {
        script {
          docker.withRegistry("", registryCredential) {
            jupyterImage.push()
          }
        }
      }
    }

    stage("Deploy documentation") {
      agent {
        docker {
          alwaysPull true
          image 'lsstts/develop-env:develop'
          args "-u root --entrypoint=''"
        }
      }
      when {
        anyOf {
          changeset "docs/*"
        }
      }
      steps {
        script {
          sh "pwd"
          sh """
            source /home/saluser/.setup_dev.sh
            pip install ltd-conveyor
            ltd upload --product love-simulator --git-ref ${GIT_BRANCH} --dir ./docs
          """
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
    stage("Trigger main deployment") {
      when {
        branch "main"
      }
      steps {
        build(job: '../LOVE-integration-tools/main', wait: false)
      }
    }
  }
}
