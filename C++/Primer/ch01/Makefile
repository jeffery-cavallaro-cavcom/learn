CXX = g++
CXXFLAGS = -Wall
LINT = cpplint
LINTARGS = --root C++

PROGRAMS = hello add

LIBRARIES = libutil.a

SOURCES = input.h input.cc hello.cc

all: $(LIBRARIES) $(PROGRAMS)

libutil.a: input.o
	$(AR) $(ARFLAGS) $@ $^

input.o: input.h input.cc

hello: hello.cc

add: add.cc $(LIBRARIES)

lint:
	$(LINT) $(LINTARGS) $(SOURCES)

clean:
	rm -rf *.o $(LIBRARIES) $(PROGRAMS)
