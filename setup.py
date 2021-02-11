from setuptools import setup
# python3 setup.py py2app --includes objc,AppKit,distutils.version,timeit,cProfile

plist = dict( 
	NSPrincipalClass='GlyphsPythonModul',
	CFBundleIdentifier="com.GeorgSeifert.GlyphsPythonModul",
	NSHumanReadableCopyright="Copyright, Georg Seifert, 2021",
	CFBundleShortVersionString="1.1",
	CFBundleVersion="3",
	MinGlyphsVersion="3.0.2",
)
setup(
	plugin = ['GlyphsPythonModul.py'],
    setup_requires=["py2app"],
	options = dict(py2app=dict( 
				extension='.glyphsPlugin',
					plist=plist,
	),
	),
)