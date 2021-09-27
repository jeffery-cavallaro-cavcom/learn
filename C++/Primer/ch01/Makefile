CXX = g++-9
CC = g++-9

CXXFLAGS = -g -Wall -std=c++17

PROGRAMS = hello add sum bomb average counter

OBJS = hello.o add.o sum.o bomb.o average.o counter.o

SOURCES = hello.cc add.cc sum.cc bomb.cc average.cc counter.cc

all: $(PROGRAMS)

hello: hello.o

add: add.o

sum: sum.o

bomb: bomb.o

average: average.o

counter: counter.o

lint:
	@cpplint $(SOURCES)

clean:
	@rm -f $(PROGRAMS) $(OBJS)
