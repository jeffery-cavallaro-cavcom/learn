CXX=g++

CXXFLAGS=-g -Wall --std=c++17

LIBRARIES=libsales.a

PROGRAMS=add2 average bomb hello repeats salestest

SOURCES=*.cc

all: $(LIBRARIES) $(PROGRAMS)

libsales.a: sales_item.o
	$(AR) $(ARFLAGS) $@ $?

sales_item.o: sales_item.cc sales_item.h

add2: add2.cc
average: average.cc
bomb: bomb.cc
hello: hello.cc
repeats: repeats.cc
salestest: salestest.cc libsales.a

lint:
	@cpplint $(SOURCES)

clean:
	rm -rf $(PROGRAMS) $(LIBRARIES) *.o
