import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="codimage",
    version="0.0.1",
    description="Encrypt codes and files into picture",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ianforme/codimage",
    author="Sun Weiran",
    author_email="sunwrn@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["codimage"],
    include_package_data=True,
    install_requires=["numpy", "pillow"]
)