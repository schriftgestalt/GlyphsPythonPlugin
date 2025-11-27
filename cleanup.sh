#!/bin/sh

set -e

bundle='./Python.framework/Versions/Current'

find . -type d -name '__pycache__' -exec rm -rf {} +
rm -rf $bundle/Resources/English.lproj
rm -rf $bundle/Resources/Python.app
rm -rf $bundle/share
rm -rf $bundle/Frameworks/Tcl.framework
rm -rf $bundle/Frameworks/Tk.framework
