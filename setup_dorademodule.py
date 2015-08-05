#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

setup(name="DoradeModule",
	ext_modules=[
	Extension("Dorade",["dorademodule.cpp"],
				include_dirs=['/home/raul/Github/boost_python','/home/raul/miniconda/pkgs/qt-4.8.6-3/include/QtCore'],
				library_dirs=['/home/raul/miniconda/pkgs/qt-4.8.6-3/lib'],
				libraries = ["boost_python","QtCore"])
	])
