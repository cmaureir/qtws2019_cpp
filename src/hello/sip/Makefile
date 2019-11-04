TARGET = simple.so
OFILES = sipsimplecmodule.o
HFILES = sipAPIsimple.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -I. -I/home/cmaureir/repos/unleash_cpp/env/include/python3.7m -I/home/cmaureir/python/3.7.3g/include/python3.7m
CFLAGS = -pipe -fPIC -O2 -Wall -W
CXXFLAGS = -pipe -fPIC -O2 -Wall -W
LFLAGS = -shared -Wl,--version-script=simple.exp
LIBS = -lsimple
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	@echo '{ global: PyInit_simple; local: *; };' > simple.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/home/cmaureir/repos/unleash_cpp/env/lib/python3.7/site-packages || mkdir -p $(DESTDIR)/home/cmaureir/repos/unleash_cpp/env/lib/python3.7/site-packages
	cp -f $(TARGET) $(DESTDIR)/home/cmaureir/repos/unleash_cpp/env/lib/python3.7/site-packages/$(TARGET)
	strip $(DESTDIR)/home/cmaureir/repos/unleash_cpp/env/lib/python3.7/site-packages/$(TARGET)

clean:
	-rm -f $(TARGET)
	-rm -f sipsimplecmodule.o
	-rm -f simple.exp
