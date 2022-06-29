## Update instructions
- Download the latest universal binary release from python.org and install it.
- Copy the Python.framework from `/Library/Frameworks/Python.framework`
- Remove the following files and folders:
	- All other versions that might be in the `Versions` folder. 
	- Python.framework/Versions/3.XX/lib/python3.10/test
	- Python.framework/Versions/3.XX/Resources/English.lproj
	- Python.framework/Versions/3.XX/Resources/Python.app
	- Python.framework/Versions/3.XX/share
	- all `__pycache__` folders