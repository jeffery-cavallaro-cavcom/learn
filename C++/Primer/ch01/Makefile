CXX = g++

CC = g++

CXXFLAGS = -g -Wall --std=c++17 $(INCLUDES)

INCLUDES =

SOURCES = \
	add2.cc \
	average.cc \
	bomb.cc \
	hello.cc \
	repeats.cc \
	sales_item.cc \
	salestest.cc

PROGRAMS = add2 average bomb hello repeats salestest

LIBRARIES = libsales.a

all: $(LIBRARIES) $(PROGRAMS)

libsales.a: sales_item.o
	$(AR) $(ARFLAGS) $@ $?

add2: add2.o
average: average.o
bomb: bomb.o
hello: hello.o
repeats: repeats.o
salestest: salestest.o -lsales

lint:
	cpplint --root=. *.h *.cc

clean:
	rm -f $(PROGRAMS) $(LIBRARIES) *.o *.d

.PHONY: help dummy

help:
	@echo
	@$(MAKE) -f $(word 1, ${MAKEFILE_LIST}) -p -q dummy | \
	grep -v -e '^dummy' | \
	awk '/^[^.%][-A-Za-z0-9_]*:/ \
		{ print substr($$1, 1, length($$1)-1) }' | \
	sort | \
	pr -4 -T -w 80
	@echo

dummy:

include $(subst .cc,.d,$(SOURCES))

%.d: %.cc
	@ $(CXX) -M $(CPPFLAGS) $< > $@.$$$$;                      \
	sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@;     \
	rm -f $@.$$$$
