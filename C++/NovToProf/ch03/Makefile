-include ~/make/cpp.mak

SIMPLE_PROGRAMS = bits

PROGRAMS = $(SIMPLE_PROGRAMS)

SOURCES = bits.cc

all: $(PROGRAMS)

$(SIMPLE_PROGRAMS): %: %.cc
	$(LINK.o) $(OUTPUT_OPTION) $<

lint:
	@$(LINT.cc) $(INCLUDES) $(SOURCES)

clean:
	@${RM} -f $(PROGRAMS)

distclean: clean
	@${RM} -f *.d

include $(TEMPLATES)/util.mak
