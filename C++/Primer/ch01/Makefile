CXX = g++-9
CC = g++-9

CXXFLAGS = -g -Wall -std=c++17

PROGRAMS = hello add sum bomb average counter sales

LIBRARIES = libbookstore.a

OBJS = hello.o add.o sum.o bomb.o average.o counter.o sales_item.o sales.o

SOURCES =	hello.cc \
			add.cc \
			sum.cc \
			bomb.cc \
			average.cc \
			counter.cc \
			sales_item.h \
			sales_item.cc \
			sales.cc

all: $(LIBRARIES) $(PROGRAMS)

hello: hello.o

add: add.o

sum: sum.o

bomb: bomb.o

average: average.o

counter: counter.o

libbookstore.a: sales_item.h sales_item.o
	$(AR) $(ARFLAGS) libbookstore.a sales_item.o

sales: sales.o libbookstore.a
	$(CC) -o sales sales.o -L . -lbookstore

lint:
	@cpplint $(SOURCES)

clean:
	@rm -f $(LIBRARIES) $(PROGRAMS) $(OBJS)
