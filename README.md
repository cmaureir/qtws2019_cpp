# Qt World Summit 2019 Berlin
## How to bring your C++ projec to Python land

There has been always efforts to provide Python bindings for many popular C++
libraries and frameworks.

This binding process is a complex task, and there has been many tools that tried to
achieve t in different ways.

Due to the complexity of some libraries, one needs to wisely choose the elements
that will form this entire process.

In the case of Qt, after a proper study, it became apparent that a custom solution
was required, and this led to the creation of Shiboken, which is the bindings
generator tool behind the Qt for Python project.

In this talk, you will learn how to get started with many binding generation tools,
but most importantly we will go step-by-step on how to start your own binding
project using Shiboken.

### Examples

The examples contain a simple implementation of a `Hello World`
written in C and C++, then a basic implementation using different tools
is used to expose the function to Python.

* `cpython`, using a simple raw CPython implementation for the function.
* `ctypes`, to load the shared library (not used in the talk).
* [Boost::python](https://www.boost.org/doc/libs/1_61_0/libs/python/doc/html/index.html)
* [SWIG](http://www.swig.org/)
* [shiboken](https://doc.qt.io/qtforpython/shiboken2/)
* [pyBind11](https://pybind11.readthedocs.io)
* [cffi](https://cffi.readthedocs.io">cffi.readthedocs.io)
* [cppyy](https://cppyy.readthedocs.io)
* [sip](https://riverbankcomputing.com/software/sip)

A more useful example related to `glob` is included too in the directory
*fastglob*. This example uses the `<filesystem>` C++ library to achieve
a similar result as `glob` and `Pathlib.glob`.

* `fastglob`, directory with the implementation of the module.
* `data`, 1000 directories with 1000 empty files each.
* `glob_list.py`, listing using `glob`.
* `pathlib_list.py`, listing using `Pathlib`.
* `fastglob_list.py`, listing using `fastglob`.
* `benchmark_1.sh`, benchmark using `/usr/bin/time`.
* `benchmark_2.py`, benchmark using `time`.

### Slides

You can check the [slides here!](https://maureira.xyz/talks/qt/qtws2019_cpp)
to write them I used [reveal.js](https://github.com/hakimel/reveal.js/).

