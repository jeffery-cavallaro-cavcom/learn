-include ~/make/cpp.mak

SIMPLE_PROGRAMS = hello add sum bomb average counter

LIB_PROGRAMS = sales

PROGRAMS = $(SIMPLE_PROGRAMS) $(LIB_PROGRAMS)

LIBRARIES = libbookstore.a

LDLIBDIRS = -L.

LDLIBS = -lbookstore

OBJS = sales_item.o sales.o

INCLUDES = sales_item.h

SOURCES =	hello.cc \
			add.cc \
			sum.cc \
			bomb.cc \
			average.cc \
			counter.cc \
			sales_item.cc \
			sales.cc

all: $(LIBRARIES) $(PROGRAMS)

$(SIMPLE_PROGRAMS): %: %.cc
	$(LINK.o) $(OUTPUT_OPTION) $<

libbookstore.a: sales_item.o
	$(AR) $(ARFLAGS) $@ $?

sales_item.o: sales_item.h

sales: sales.o $(LDLIBS)
	$(LINK.o) $(LDLIBDIRS) $(OUTPUT_OPTION) $+

lint:
	@$(LINT.cc) $(INCLUDES) $(SOURCES)

clean:
	@${RM} -f $(LIBRARIES) $(PROGRAMS) $(OBJS)

distclean: clean
	@${RM} -f *.d

help:
	@${MAKE} --print-data-base --question all | \
    grep -v -e '[Mm]akefile' -e '^[#.-]' | \
    grep -e '^[-A-Za-z0-9_]*\(.a\)*:' | \
    gawk '/.*:/ { print substr($$1,1,length($$1)-1) }' | \
    sort | \
	pr --omit-pagination --width=80 --columns=4

-include $(subst .cc,.d,$(SOURCES))
