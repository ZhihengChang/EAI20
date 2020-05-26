#Easy Edit
Easy Edit is a simple command line tool for image editing / processing
##Installation
Install requirements using `pip`:
```bash
pip install -r /path/to/requirements.txt
```
NOTE: requirements.txt should just be in the Easy Edit folder.
After install the requirements, run the program using:
```bash
python cv.py
```
##Version History
**Version 1.0**
Easy Edit version 1.0 is the initial version.Supports:
Basics:
* h: Display program help center.
* s: Save image to local machine.
* q: Quit program.
Image Editing / processing:
* Read: Read input image name from loacal machine. Reading Path: `/img`
* Show: Display read image. 
* Write: Write input text on the read image at input position. Text colors: red, green, blue
* Rotate: Rotate read image by input degrees.
* Status: Display program status. 
