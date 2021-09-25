CXX = g++
CC = g++

CXXFLAGS = -g -Wall -std=c++17

PROGRAMS = answer

OBJS = answer.o

SOURCES = answer.cc

all: $(PROGRAMS)

hello: hello.o

lint:
	@cpplint $(SOURCES)

clean:
	@rm -f $(PROGRAMS) $(OBJS)
