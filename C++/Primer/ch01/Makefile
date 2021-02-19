CXX = g++
CXXFLAGS = -Wall
LINT = cpplint
LINTARGS = --root C++

PROGRAMS = hello add range bomb

LIBRARIES = libutil.a

SOURCES = input.h input.cc hello.cc range.cc bomb.cc

all: $(LIBRARIES) $(PROGRAMS)

libutil.a: input.o
	$(AR) $(ARFLAGS) $@ $^

input.o: input.h input.cc

hello: hello.cc

add: add.cc $(LIBRARIES)

range: range.cc $(LIBRARIES)

bomb: bomb.cc $(LIBRARIES)

lint:
	$(LINT) $(LINTARGS) $(SOURCES)

clean:
	rm -rf *.o $(LIBRARIES) $(PROGRAMS)
