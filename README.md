# codimage

codimage is a Python library that encrypts single / multiple text-transferrable files, i.e. Python scripts, batch scripts and configuration files, into a single picture and protect your information with password.

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
codimage.encrypt(original-png-file-path,
                 path-to-the-file,
                 export-pnd-file-path,
                 password)
```

#### Multiple files encryption

assume files to be encrypted are in D:\codes folder

```python
codimage.encrypt(original-png-file-path,
                 r"D:\codes",
                 export-pnd-file-path,
                 password)
```

#### Image decryption

assume files are to be exported to D:\export-codes

```python
codimage.decrypt(original-png-file-path,
                 encrypted-png-file-path,
                 r"D:\export-codes",
                 password)
```

After decryption,  a folder named 'codimage-*datetime*' will be created in export-codes with all files inside

## License

The software is under MIT License

