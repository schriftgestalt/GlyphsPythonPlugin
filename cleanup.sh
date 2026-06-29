#!/bin/sh

set -e

bundle='./Python.framework/Versions/Current'

find . -type d -name '__pycache__' -exec rm -rf {} +
find $bundle/lib -type d -name '*.dSYM' -exec rm -rf {} +
rm -rf $bundle/Resources/English.lproj
rm -rf $bundle/Resources/Python.app
rm -rf $bundle/share
rm -rf $bundle/Frameworks
rm -rf $bundle/lib/python3.*/test
rm -rf $bundle/lib/python3.*/idlelib
rm -rf $bundle/lib/python3.*/site-packages/PyObjCTest