## Update instructions
- Download the latest universal binary release from python.org and install it.
- Copy the Python.framework from `/Library/Frameworks/Python.framework`
- run `pip3 install pyobjc` (this should install an universal binary)
- run `pip3 install brotli` (this should install an universal binary)
- Remove the following files and folders:
	- All other versions that might be in the `Versions` folder. 
	- from Python.framework/Versions/3.XX/lib/python3.xx/
		- test
		- idlelib
		- unittest
		- distutils
		- tk8.6
		- Tk.tiff
		- Tk.icns
		- tkConfig.sh
		- libtk8.6.dylib
		- libtcl8.6.dylib
		- tcl8.6
		- site-packages/pip
		- site-packages/setuptools
	- from Python.framework/Versions/3.XX/lib
		- tcl8
		- libtclstub8.6.a
		- libtkstub8.6.a
	- Python.framework/Versions/3.XX/Resources/English.lproj
	- Python.framework/Versions/3.XX/Resources/Python.app
	- Python.framework/Versions/3.XX/share
	- all `__pycache__` folders