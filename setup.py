import os
from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

version="0.0.1"

if "GITHUB_RUN_ID" in os.environ:
    version += "-"
    version += os.environ["GITHUB_RUN_ID"]

ext = Extension(
    "ciostream",
    sources=[
        "src/ciostream/__init__.pyx",
        "src/ciostream/ciostream_native.cpp"],
    language="c++")

setup(
    name="ciostream",
    version=version,
    author="Matthew Ballance",
    author_email="matt.ballance@gmail.com",
    description="Provides C++ iostream Cython wrappers",
    zip_safe=False,
    packages = ['ciostream'],
    package_dir = {'': 'src'},
    package_data = {
        'ciostream': ['*.pxd', '*.cpp', '*.h']
    },
    ext_modules = cythonize([ext],
                    compiler_directives={
                        'embedsignature': True,
                        'language_level': '3str'})
)

