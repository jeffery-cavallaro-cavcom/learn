CXX = g++
CXXFLAGS = -Wall
LINT = cpplint

PROGRAMS = hello

SOURCES = hello.cc

all:	$(PROGRAMS)

hello:	hello.cc

lint:
	$(LINT) $(SOURCES)

clean:
	rm $(PROGRAMS)
