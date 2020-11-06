#!/bin/bash

set -e

if [ $(git branch --show-current) != "master" ]; then
  echo "Not on master branch"
  exit 1
fi


if test -z "$(git status --porcelain 2>/dev/null| grep \"^??\" | wc -l)"; then
  echo "Git has untracked files"
  exit 1
fi

if test -n "$(git status --porcelain)"; then
  echo "Git is dirty"
  exit 1
fi


pip install "setuptools>=38.6.0"
pip install "twine>=1.11.0"
python setup.py sdist
