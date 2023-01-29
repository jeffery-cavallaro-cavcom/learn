CXX=g++

CXXFLAGS=-g -Wall --std=c++17

PROGRAMS=conversions types

SOURCES=*.cc

all: $(PROGRAMS)

conversions: conversions.cc
types: types.cc

lint:
	@cpplint $(SOURCES)

clean:
	rm -rf $(PROGRAMS) *.o
