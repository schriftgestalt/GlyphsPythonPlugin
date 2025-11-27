## Update instructions

- remove "Python.framework"

- run `python3 relocatable-python/make_relocatable_python_framework.py --python-version 3.XX.Y --destination . --os-version 11`

- run `./Python.framework/Versions/Current/bin/python3 -m pip install pyobjc brotli` (this should install an universal binary)

- Remove the following files and folders:
	- All other versions that might be in the `Versions` folder. 
	- from Python.framework/Versions/3.XX/lib/python3.xx/
		- test
		- idlelib
		- distutils
		- tk8.6
		- Tk.tiff
		- Tk.icns
		- tkConfig.sh
		- libtk8.6.dylib
		- libtcl8.6.dylib
		- libtclstub8.6.a
		- libtkstub8.6.a
		- tcl8.6
		- site-packages/setuptools
	- from Python.framework/Versions/3.XX/lib
		- tcl8
		- libtclstub8.6.a
		- libtkstub8.6.a
	- Python.framework/Versions/3.XX/Resources/English.lproj
	- Python.framework/Versions/3.XX/Resources/Python.app
	- Python.framework/Versions/3.XX/share
	- all `__pycache__` folders