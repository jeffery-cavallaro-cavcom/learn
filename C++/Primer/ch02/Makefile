-include ~/make/cpp.mak

SIMPLE_PROGRAMS = limits convert literals initial scope ref

PROGRAMS = $(SIMPLE_PROGRAMS) global

SOURCES = limits.cc \
          convert.cc \
          declare.cc \
          define.cc \
          literals.cc \
          initial.cc \
          ref.cc

OBJS = declare.o define.o

all: $(PROGRAMS)

$(SIMPLE_PROGRAMS): %: %.cc
	$(LINK.o) $(OUTPUT_OPTION) $<

global: define.o declare.o
	$(LINK.o) $(OUTPUT_OPTION) $+

lint:
	@$(LINT.cc) $(INCLUDES) $(SOURCES)

clean:
	@${RM} -f $(LIBRARIES) $(PROGRAMS) $(OBJS)

distclean: clean
	@${RM} -f *.d

include $(TEMPLATES)/util.mak
