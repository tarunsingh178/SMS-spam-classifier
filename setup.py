from setuptools import setup

fh=open("readme.md", "r")
long_description=fh.read()

AUTHOR_NAME='Tarun Kumar Singh'
SRC_REPO='src'
LIST_OF_REQUIREMENTS = ['streamlit','nltk','sklearn']

setup(
    name= SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='tarunshivam3@gmail.com',
    description='A simple python package for creating a web app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.6',
    install_requires=LIST_OF_REQUIREMENTS,
)
