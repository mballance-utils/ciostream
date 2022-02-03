
from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

ext = Extension(
    "testext",
    sources=[
        "testext/__init__.pyx",
        "testext/StreamReader.cpp",
        "testext/StreamWriter.cpp"
        ],
    language="c++")

setup(
    name="testext",
    version="0.0.1",
    author="Matthew Ballance",
    author_email="matt.ballance@gmail.com",
    description="Provides C++ iostream Cython wrappers",
    zip_safe=False,
    packages = ['testext'],
    ext_modules = cythonize([ext])
)

