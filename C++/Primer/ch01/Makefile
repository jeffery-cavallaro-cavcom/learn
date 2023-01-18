CXX=g++

CXXFLAGS=-g -Wall --std=c++17

PROGRAMS=add2 average bomb hello repeats

SOURCES=*.cc

all: $(PROGRAMS)

add2: add2.cc
average: average.cc
bomb: bomb.cc
hello: hello.cc
repeats: repeats.cc

lint:
	@cpplint $(SOURCES)

clean:
	rm -rf $(PROGRAMS) *.o
