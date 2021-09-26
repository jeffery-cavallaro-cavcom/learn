CXX = g++
CC = g++

CXXFLAGS = -g -Wall -std=c++17

PROGRAMS = hello add

OBJS = hello.o add.o

SOURCES = hello.cc add.cc

all: $(PROGRAMS)

hello: hello.o

add: add.o

lint:
	@cpplint $(SOURCES)

clean:
	@rm -f $(PROGRAMS) $(OBJS)
