# Development Guide

If you already cloned the repository and you know that you need to deep dive in the code, here are some guidelines to set up your environment.

!! NOTICE

## Installation

Virtual environment with `pyenv`

-----------------

Please check the following repo for how to install pyenv

[github.com/pyenv/pyenv](https://github.com/pyenv/pyenv#installation)

### Install Python 3.10 with `pyenv`

```bash

export PYTHON_CONFIGURE_OPTS="--enable-framework"
export PYTHON_CONFIGURE_OPTS="--enable-shared"

pyenv install 3.10.0rc2
```

### Create a virtual environment and activate virtual environment

```bash
pyenv virtualenv 3.10.0rc2 ProjectHQME
pyenv activate ProjectHQME
```
