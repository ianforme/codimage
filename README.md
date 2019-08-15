# codimage

codimage is a Python library that encrypts single / multiple text-transferable files, i.e. Python scripts, batch scripts and configuration files, into a single picture and protect your information with password.

## Overview

#### File encryption

Given a single / multiple files, a **PNG** image (your own selfies will also work!), and a user defined password, codimage will generate a **PNG** image that is nearly identical to the original one with all contents from the files to be encrypted into the pixels. 

#### File decryption

To decrypt and reverse back files from the code embedded image, user needs to use the original image and the correct password. 

## Installation

```bash
pip install codimage
```

## Usage

#### Single file encryption

```python
from codimage import codimage

codimage = codimage.Codimage()
codimage.encrypt(r"D:\dummy\dummy.png",
                 r"D:\codes\test.py",
                 r"D:\dummy\code.png",
                 "P@ssw0rd1")
```

#### Multiple files encryption

assume files to be encrypted are in D:\codes folder

```python
codimage.encrypt(r"D:\dummy\dummy.png",
                 r"D:\codes",
                 r"D:\dummy\code.png",
                 "P@ssw0rd1")
```

#### Image decryption

assume files are to be exported to D:\export-codes

```python
codimage.decrypt(r"D:\dummy\dummy.png",
                 r"D:\dummy\code.png",
                 r"D:\export-codes",
                 "P@ssw0rd1")
```

After decryption,  a folder named 'codimage-*datetime*' will be created in export-codes with all files inside

## License

The software is under MIT License

