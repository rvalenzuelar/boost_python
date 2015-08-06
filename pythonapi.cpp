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

namespace bp = boost::python;


/*** wrapping functions ***/
float getElevation(Dorade &foo, int x)
{
	return foo.getElevation(x);
}

bp::list getReflectivity(Dorade &foo, int ray_indx)
{
	if (ray_indx>=foo.getNumRays()){
		bp::list a;
		return a;
	}

	float* y = foo.getReflectivity(ray_indx);
	bp::list a;
	for (int gate=0; gate<foo.getNumGates(); gate++)
	{
		a.append(y[gate]);
	}
	return bp::list(a);
	delete y;
}


BOOST_PYTHON_MODULE(Dorade)
{

	initializeConverters(); // included in boost_converter.h

	bp::class_<Dorade>("Dorade")
		.def(init<const QString&>())
		.def("getFilename", &Dorade::getFilename)
		.def("getNumRays", &Dorade::getNumRays)
		.def("getNumGates", &Dorade::getNumGates)
		.def("getElevation", getElevation)
		.def("getReflectivity", getReflectivity);
}
