import os
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

version="0.0.1"

# CI stamps a PEP 440 LOCAL VERSION SEGMENT onto everything that is not a tag
# build, e.g. "dev33020374597+gh.g7775f37" -> 0.0.1.dev33020374597+gh.g7775f37.
#
# This replaced `version += "-" + GITHUB_RUN_ID`, which was wrong in two ways
# that both mattered. It normalised to 0.0.1-33020374597 -> "0.0.1.post33020374597",
# which PEP 440 sorts AFTER the release it was built from, so a CI build of an
# unreleased commit outranked the release itself. And it carried no marker for
# WHICH forge built it -- both GitHub and Forgejo build every commit and their
# run ids are different counters, so the id alone collides.
#
# `.dev` sorts before the release, and a local segment is rejected outright by
# PyPI -- so "a CI artifact can never become a release" is enforced by the
# packaging standard rather than by an `if:` we would have to get right.
build_num = os.environ.get("BUILD_NUM", "").strip()
if build_num:
    version = version + "." + build_num

ext = Extension(
    "ciostream.core",
    sources=[
        "src/ciostream/core.pyx",
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
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    packages = ['ciostream'],
    package_dir = {'': 'src'},
    package_data = {
        # '*.pyx' was missing, and that made every sdist this project has ever
        # published unbuildable: `pip install ciostream` from source fetched a
        # tarball with core.pxd but no core.pyx, and died in cythonize() with
        # "'src/ciostream/core.pyx' doesn't match any files". It was invisible
        # locally because a previously-generated core.cpp sits in the tree.
        'ciostream': ['*.pyx', '*.pxd', '*.cpp', '*.h', '*.lib']
    },
    # entry_points={
    #     "ivpm.pkginfo": [
    #         'ciostream = ciostream.pkginfo:PkgInfo'
    #     ]
    # },
    # cythonize() rather than handing setuptools the .pyx directly: the implicit
    # path depends on setuptools noticing Cython is importable, which is exactly
    # the thing that broke when setup_requires stopped resolving.
    ext_modules=cythonize([ext], language_level="3")
)

