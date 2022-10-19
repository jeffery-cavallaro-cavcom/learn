CXX=g++

CXXFLAGS=-g -Wall --std=c++17

PROGRAMS=hello add2 average bomb

SOURCES=*.cc

all: $(PROGRAMS)

hello: hello.cc

add2: add2.cc

average: average.cc

bomb: bomb.cc

lint:
	@cpplint $(SOURCES)

clean:
	rm -rf $(PROGRAMS) *.o
