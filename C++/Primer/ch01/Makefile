CXX = g++
CC = g++

CXXFLAGS = -g -Wall -std=c++17

PROGRAMS = hello

OBJS = hello.o

SOURCES = hello.cc

all: $(PROGRAMS)

hello: hello.o

lint:
	@cpplint $(SOURCES)

clean:
	@rm -f $(PROGRAMS) $(OBJS)
