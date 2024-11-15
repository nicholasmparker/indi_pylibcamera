
from setuptools import setup, find_packages

setup(
    name="indi_pylibcamera",
    version="0.9.0",
    description="INDI driver for Raspberry Pi cameras using libcamera",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nicholas Parker",
    author_email="nicholasmparker@gmail.com", 
    url="https://github.com/nicholasmparker/indi_pylibcamera",
    packages=find_packages(),
    install_requires=[
        "astropy",
        "numpy",
        "picamera2",
    ],
    entry_points={
        "console_scripts": [
            "indi_pylibcamera=indi_pylibcamera.indi_pylibcamera:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
)
