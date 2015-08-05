/*
	API for connecting Dorade C++ class with python

	Sources: 
	https://github.com/abingham/boost_python_tutorial/blob/master/workshop/Boost.Python.workshop.ipynb
	http://urtconnector.googlecode.com/svn/branches/python/src/python/api/urtapi.cpp

	Raul Valenzuela
	August, 2015

*/

#include <boost/python.hpp>
#include <dorademodule.h>
#include <QString>
#include "boost_converter.h"

using namespace boost::python;

/*** wrapping functions ***/
float getElevation(Dorade &foo, int x)
{
	float y = foo.getElevation(x);
	return y;
}

BOOST_PYTHON_MODULE(Dorade)
{

	initializeConverters(); // included in boost_converter.h

	class_<Dorade>("Dorade")
		.def(init<const QString&>())
		.def("getFilename", &Dorade::getFilename)
		.def("readSwpfile",&Dorade::readSwpfile)
		.def("getNumRays", &Dorade::getNumRays)
		.def("getNumGates", &Dorade::getNumGates)
		.def("getElevation", getElevation);
}
