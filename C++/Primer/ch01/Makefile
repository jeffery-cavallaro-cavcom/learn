CXX = g++
CXXFLAGS = -Wall
LINT = cpplint
LINTARGS = --root C++

PROGRAMS = hello add range bomb sum dups

LIBRARIES = libutil.a

SOURCES = input.h input.cc util.h util.cc hello.cc range.cc bomb.cc sum.cc

all: $(LIBRARIES) $(PROGRAMS)

libutil.a: input.o util.o
	$(AR) $(ARFLAGS) $@ $^

input.o: input.h input.cc

util.o: util.h util.cc

hello: hello.cc

add: add.cc $(LIBRARIES)

range: range.cc $(LIBRARIES)

bomb: bomb.cc $(LIBRARIES)

sum: sum.cc

dups: dups.cc

lint:
	$(LINT) $(LINTARGS) $(SOURCES)

clean:
	rm -rf *.o $(LIBRARIES) $(PROGRAMS)
