#!/usr/bin/env python

"""
Setup script for making Dorade module available in python

Raul Valenzuela
August, 2015

"""

from distutils.core import setup
from distutils.extension import Extension

# boost_headers = '/home/raul/Github/boost_python'
# qt_headers = '/home/raul/miniconda/pkgs/qt-4.8.6-3/include/QtCore'
# qt_libs = '/home/raul/miniconda/pkgs/qt-4.8.6-3/lib'

boost_headers = '/home/rvalenzuela/Github/boost_python'
qt_headers = '/home/rvalenzuela/miniconda/pkgs/qt-4.8.6-3/include/QtCore'
qt_libs = '/home/rvalenzuela/miniconda/pkgs/qt-4.8.6-3/lib'

setup(name="DoradeModule",
	ext_modules=[
	Extension("Dorade",["dorademodule.cpp","pythonapi.cpp"],
				include_dirs=[boost_headers, qt_headers],
				library_dirs=[qt_libs],
				libraries = ["boost_python","QtCore"])
	])
