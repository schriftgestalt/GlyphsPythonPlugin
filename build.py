import os

projectFolder = os.path.dirname(__file__)

buildRoot = os.path.join(projectFolder, "dist/GlyphsPythonModul.glyphsPlugin")
#os.system("python3 setup.py py2app --includes objc,AppKit,distutils.version,timeit,cProfile")

for (dirpath, dirnames, filenames) in os.walk(buildRoot):
	for filename in filenames:
		if filename.endswith(".so"):
			binPath = os.path.join(dirpath, filename)
			codesignCommand = 'codesign --remove-signature "%s"' % (binPath)
			os.system(codesignCommand)

binaries = [os.path.join(buildRoot, "Contents/Frameworks/Python.framework/Versions/3.8/Python")]
for binary in binaries:
	codesignCommand = 'codesign --remove-signature "%s"' % (binary)
	os.system(codesignCommand)

codesignCommand = 'codesign --deep --remove-signature "%s"' % (buildRoot)
os.system(codesignCommand)