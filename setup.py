from setuptools import setup

setup(
    name='breezypythongui', 
    version='1.1.1',
    author='Ken Lambert',
    author_email='lambertk@wlu.edu',
    description='A simple GUI toolkit for Python',
    packages=['breezypythongui'],  # Include the package directory
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
