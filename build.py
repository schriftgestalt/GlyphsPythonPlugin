import os

projectFolder = os.path.dirname(__file__)

buildRoot = os.path.join(projectFolder, "dist/GlyphsPythonModul.glyphsPlugin")
os.system("python3 setup.py py2app --includes objc,AppKit,distutils.version,timeit,cProfile")

for (dirpath, dirnames, filenames) in os.walk(buildRoot):
	for filename in filenames:
		if filename.endswith(".so"):
			binPath = os.path.join(dirpath, filename)
			ibtoolCommand = 'codesign --force -s "Developer ID Application: Georg Seifert" "%s"' % (binPath)
			os.system(ibtoolCommand)

ibtoolCommand = 'codesign --deep --force -s "Developer ID Application: Georg Seifert" "%s"' % (buildRoot)
