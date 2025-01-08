from setuptools import setup, find_packages

setup(
    name='breezypythongui',
    version='1.1.2',         
    author='Ken Lambert',
    author_email='lambertk@wlu.edu',
    description='A simple GUI toolkit for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
