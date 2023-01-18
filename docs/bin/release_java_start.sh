#!/bin/sh

if [ $# -ne 1 ];then
  echo "usage: $0 <release name>"
  echo "example1: $0 1.1.1"
  exit 1
fi

version=$1

echo "milestone version: $version"

cp ./build/git/hooks/* .git/hooks

git flow release start -F $version

git flow release publish $version
