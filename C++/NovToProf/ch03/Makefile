-include ~/make/cpp.mak

SIMPLE_PROGRAMS = bits enums

PROGRAMS = $(SIMPLE_PROGRAMS)

SOURCES = bits.cc enums.cc

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
