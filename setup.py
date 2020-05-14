#from distutils.core import setup
from setuptools import setup
# python3 setup.py py2app --includes objc,AppKit,distutils.version,timeit,cProfile

plist = dict( 
	NSPrincipalClass='GlyphsPythonModul',
	CFBundleIdentifier = "com.GeorgSeifert.GlyphsPythonModul",
	NSHumanReadableCopyright = "Copyright, Georg Seifert, 2020",
)
setup(
	plugin = ['GlyphsPythonModul.py'],
	options = dict(py2app=dict( 
				extension='.glyphsPlugin',
					plist=plist,
	),
	#install_requires=["pyobjc-framework-Cocoa"],
	#setup_requires=["py2app"],
	),
)