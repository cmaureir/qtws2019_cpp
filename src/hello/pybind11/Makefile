all:
	g++ -O3 -Wall -shared -std=c++11 -fPIC `python -m pybind11 --includes` simple.cpp -o simple`python-config --extension-suffix`
clean:
	rm -rf *.so
