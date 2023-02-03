CXX=g++

CXXFLAGS=-g -Wall --std=c++17

PROGRAMS=conversions literals types

SOURCES=*.cc

all: $(PROGRAMS)

conversions: conversions.cc
literals: literals.cc
types: types.cc

lint:
	@cpplint $(SOURCES)

clean:
	rm -rf $(PROGRAMS) *.o
