char const* hello()
{
   return "Hello Qt World Summit 2019!";
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(simple)
{
    using namespace boost::python;
    def("hello", hello);
}
