CXX=g++

CXXFLAGS=-g -Wall --std=c++17

PROGRAMS=types

SOURCES=*.cc

all: $(PROGRAMS)

types: types.cc

lint:
	@cpplint $(SOURCES)

clean:
	rm -rf $(PROGRAMS) *.o
