[![Build Status](https://travis-ci.org/adumasphi/travis-tutorial.svg?branch=master)](https://travis-ci.org/adumasphi/travis-tutorial)

# Install instructions

Make sure you have a github account:
https://github.com/join

Make sure you have python installed with pytest and numpy.  If you
don't have a python install you are already familiar with, the
simplest is to install miniconda (full instructions at
https://conda.io/docs/install/quick.html). Once this is done, type the
following command in a terminal:
```bash
conda install pytest numpy
```

# Checking your install

To make sure everything is installed correctly, please run the
following commands in a terminal:

```bash
git clone https://github.com/lesteve/travis-tutorial
cd travis-tutorial
pytest # note use py.test if you are using a version of pytest < 3

```

It should give an output similar to this:

```
======================================================== test session starts ========================================================
platform linux -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
rootdir: /tmp/travis-tutorial, inifile: 
plugins: cov-2.3.1
collected 1 items 

test_all.py .

===================================================== 1 passed in 0.00 seconds ======================================================
```

# Travis docker image

Depending on available time we may cover how to debug Travis failures
on your local machine with docker. If you are
interested by this, you may want to pull the docker image before the workshop:

```bash
docker pull travisci/ci-garnet:packer-1478744932
```
