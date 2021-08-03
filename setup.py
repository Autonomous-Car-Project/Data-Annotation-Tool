# License.  (https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode

from sys import platform
from setuptools import setup, find_packages 
from codecs import open 
from os import path 

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding='utf-8') as f:
    long_description = f.read() 

setup(
    name="Data_Annotation_Tool",
    version="1.0.0",
    description = "Tools for Annotating data for Object Detection, Lane Detection and Semantic Segmentation.",
    long_description = long_description,
    url = "https://github.com/Autonomous-Car-Project/Data-Annotation-Tool",
    author="TiVRA AI",
    author_email="support@tivraai.com",
    license="Creative Commons Attribution-NonCommercial-ShareAlike 4.0. https://creativecommons.org/licenses/by-nc-sa/4.0/",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    platform = ['any'],
    keywords='tivra ai data annotation cc india tivraai data-annotation-tool self-driving autonomous',
    packages=find_packages(exclude=["docs"]),
    install_requires=[
        'pyside6', 
    ],
    entry_points={
        'console_scripts' : [
            'data_ann=anntools.main:main'
        ]
    }
) 