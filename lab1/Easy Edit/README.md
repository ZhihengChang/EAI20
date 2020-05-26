# Easy Edit
Easy Edit is a simple command line tool for image editing / processing
## Installation
Install requirements using `pip`:
```bash
pip install -r /path/to/requirements.txt
```
**NOTE:** requirements.txt should just be in the Easy Edit folder. <br />
After install the requirements, run the program using:
```bash
python cv.py
```
## Version History
**Version 1.1**  2020/5/26<br />
Easy Edit version 1.1 update the input format as well as few command to be more user friendly:
* **FIX** User input are now follow after `>>`
* **FIX** The image window after rotate image are now adjust to the image size
* **NEW** `s` command are now support `s filename`
* **NEW** `read` command are now support `read filename`
* **NEW** `rotate` command are now support `rotate degree`

---
**Version 1.0**  2020/5/26<br />
Easy Edit version 1.0 is the initial version.Supports: <br />
**Basics:**
* h: Display program help center.
* s: Save image to local machine.
* q: Quit program.


**Image Editing / processing:**
* Read: Read input image name from loacal machine. Reading Path: `/img`
* Show: Display read image. 
* Write: Write input text on the read image at input position. Text colors: red, green, blue
* Rotate: Rotate read image by input degrees.
* Status: Display program status. 
