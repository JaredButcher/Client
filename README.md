[![Release](https://github.com/MultimediaExtensibleGit/Client/workflows/Release/badge.svg?event=release)](https://github.com/MultimediaExtensibleGit/Client/releases/latest) [![Build](https://github.com/MultimediaExtensibleGit/Client/workflows/Build/badge.svg?branch=master)](https://github.com/MultimediaExtensibleGit/Client/actions/) [![Testing](https://github.com/MultimediaExtensibleGit/Client/workflows/Testing/badge.svg?branch=testing)](https://github.com/MultimediaExtensibleGit/Client/actions/)

# Multimedia Extensible Git (MEG) Client

* [Setup](#setup)

* [Build](#build)

## Setup

* Install [Python 3.7](https://www.python.org/downloads/) or newer.

* Install [pipenv](https://packaging.python.org/tutorials/managing-dependencies/).

* Clone the repository and execute the following command from the working copy in Python:

  `pipenv sync`

## Build

* Build single executable binary

  `pipenv run pyinstaller meg.spec`

* Build a debug executable folder

  `pipenv run pyinstaller meg-debug.spec`
