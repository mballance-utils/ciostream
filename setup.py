import os
from setuptools import setup
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
    long_description="""
    Provides a Cython wrapper around C++ iostream classes. 
    This allows users to easily wrap a Python IO stream 
    and pass it to a native library that uses C++ iostreams.
    """,
    zip_safe=False,
    packages = ['ciostream'],
    package_dir = {'': 'src'},
    package_data = {
        'ciostream': ['*.pxd', '*.cpp', '*.h', '*.lib']
    },
    # entry_points={
    #     "ivpm.pkginfo": [
    #         'ciostream = ciostream.pkginfo:PkgInfo'
    #     ]
    # },
    ext_modules=[ext]
)

