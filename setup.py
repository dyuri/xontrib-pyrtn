#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-pyrtn',
    version='0.1.0',
    license='MIT',
    author='Gyuri Horák',
    author_email='dyuri@horak.hu',
    description="Store the python return value of commands for the session.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.py']},
    platforms='any',
    url='https://github.com/dyuri/xontrib-pyrtn',
    project_urls={
        "Documentation": "https://github.com/dyuri/xontrib-pyrtn/blob/master/README.md",
        "Code": "https://github.com/dyuri/xontrib-pyrtn",
        "Issue tracker": "https://github.com/dyuri/xontrib-pyrtn/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
