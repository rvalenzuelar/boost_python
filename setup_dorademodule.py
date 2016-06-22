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

home='/home/raul'

boost_headers = home+'/Github/boost_python'
qt_qt4 = home+'/miniconda3/envs/py27/include/qt4'
qt_QtCore = home+'/miniconda3/envs/py27/include/qt4/QtCore'
qt_libs = home+'/miniconda3/envs/py27/lib'

setup(name="DoradeModule",
	ext_modules=[
	Extension("Dorade",["dorademodule.cpp","pythonapi.cpp"],
				include_dirs=[boost_headers, qt_qt4, qt_QtCore],
				library_dirs=[qt_libs],
				libraries = ["boost_python","QtCore"])
	])
