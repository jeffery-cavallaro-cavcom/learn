CXX = g++

CC = g++

CXXFLAGS=-g -Wall --std=c++17 $(INCLUDES)

INCLUDES =

SOURCES = \
	conversions.cc \
	literals.cc \
	types.cc \
	strings.cc \
	numbers.cc \
	variables.cc \
	scope.cc \
	compound.cc

PROGRAMS = \
	conversions \
	literals \
	types \
	strings \
	variables \
	scope \
	compound \
	temptest

LIBRARIES =

all: $(LIBRARIES) $(PROGRAMS)

conversions: conversions.o
literals: literals.o
types: types.o
strings: strings.o
variables: variables.o numbers.o
scope: scope.o
compound: compound.o
temptest: temptest.o

lint:
	cpplint --root=. *.cc

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
