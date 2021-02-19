CXX = g++
CXXFLAGS = -Wall
LINT = cpplint
LINTARGS = --root C++

PROGRAMS = hello add range bomb sum dups report

UTILLIBS = libutil.a
BOOKLIBS = bookstore.a

LIBRARIES = $(UTILLIBS) $(BOOKLIBS)

SOURCES = input.h input.cc util.h util.cc \
	sales_item.h sales_item.cc \
	hello.cc range.cc bomb.cc sum.cc \
	report.cc

all: $(LIBRARIES) $(PROGRAMS)

libutil.a: input.o util.o
	$(AR) $(ARFLAGS) $@ $^

bookstore.a: sales_item.o
	$(AR) $(ARFLAGS) $@ $^

input.o: input.h input.cc

util.o: util.h util.cc

sales_item.o: sales_item.h sales_item.cc

hello: hello.cc

add: add.cc $(UTILLIBS)

range: range.cc $(UTILLIBS)

bomb: bomb.cc $(UTILLIBS)

sum: sum.cc

dups: dups.cc

report: report.cc $(BOOKLIBS)

lint:
	$(LINT) $(LINTARGS) $(SOURCES)

clean:
	rm -rf *.o $(LIBRARIES) $(PROGRAMS)
