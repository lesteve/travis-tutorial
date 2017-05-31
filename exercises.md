# Set-up
Any problems with install instructions?

Fork my repo https://github.com/lesteve/travis-tutorial. Clone your
own repo:
```
git clone https://github.com/<your-github-account>/travis-tutorial
```

Activate your repo on Travis: https://travis-ci.org/your-github-account/travis-tutorial
Click on "Activate repo"

# Simple .travis.yml file
```yaml
language: python

dist: trusty

script: py.test
```

commit + push. Look at build on https://travis-ci.org/your-github-account/travis-tutorial

# Broken .travis.yml
What happens if you have a broken .travis.yml?

http://lint.travis-ci.org/
Alternative: `gem install travis` + `travis lint`.

# Pushing a commit
Add one commit (e.g. another assert) + watch the build on travis-ci.org.

# Opening a PR
Open a PR on my repo https://github.com/lesteve/travis-tutorial

Create a feature branch as the PR source and use `for-prs` as the target
branch. Maybe some conflicts will need to be solved along the line ...

Try to follow best practices and put some minimal effort in your PR
title and PR description.
# Testing on multiple Python versions
Add test_division:

Add this to `test_all.py`:
```py
def test_division():
    assert 3/2 == 1.5
```

Add this to your `.travis.yml`:
```
python:
  - 2.7
  - 3.6
```

# `install` step
New dependency: numpy.

Add a new function test_partition with a simple test.
for [numpy.partition](https://docs.scipy.org/doc/numpy/reference/generated/numpy.partition.html).

What is the numpy version (already installed in the virtualenv)? Add
print statement in .travis.yml.

Add build matrix entries with different versions of numpy (1.7.1 and 1.12.1).

Add this to your .travis.yml:
```yml
env:
  - NUMPY_VERSION=1.7.1
  - NUMPY_VERSION=1.12.1

install: pip install numpy==$NUMPY_VERSION
```

See [doc](https://docs.travis-ci.com/user/customizing-the-build) for
more details about all the build steps.

Build matrix: More explicit way of defining build matrix.
See [doc](https://docs.travis-ci.com/user/customizing-the-build#Build-Matrix)

More complicated install step: test on Ubuntu. Hint: use deactivate
and use an install script. Also look at:
[apt plugin doc](https://docs.travis-ci.com/user/installing-dependencies/#Adding-APT-Packages).

# Cache
The Python 3.6 + numpy 1.7.1 should take more time than the others,
any idea why?

cache pip dependencies by adding this to your .travis.yml file:
```yaml
cache: pip
```
Note: another useful cache setup is `cache: ccache` for C/C++ projects)

Does it have an impact on the build timings?

Do the same by caching the ~/.pip/cache folder.

Find a dummy use case to feature custom directory caching, e.g. a
function that sleeps a few seconds before returning.

Read the [caching doc](https://docs.travis-ci.com/user/caching/) and test a few things they mention:
* branch use cache from master if the branch does not have a cache yet
* per-environment cache, i.e. does multiple build matrix entries share the same cache?
* clear the cache via the web UI.

# Docker

Using continuumio/miniconda docker image, creating a conda
environment with the right python + numpy version.

# Additional things to play with
- set up Travis for your own project
- allow_failures
- Use Travis docker images to run Travis locally:
  http://eng.localytics.com/best-practices-and-common-mistakes-with-travis-ci/
- try using ccache and caching the .ccache in scikit-learn, is it
  faster (if yes by how much) than compiling each time from scratch.
  How big does the cache grow (i.e. ccache defaults)? How much time
  does it take to restore. What is a reasonable cache size to set ?
  How quickly does the cache grow ?

# Useful documentation pages
Some useful documentation pages:
https://docs.travis-ci.com/user/customizing-the-build
https://docs.travis-ci.com/user/languages/python/
https://docs.travis-ci.com/user/ci-environment/
https://docs.travis-ci.com/user/caching/
https://docs.travis-ci.com/user/docker/
https://docs.travis-ci.com/user/common-build-problems/
