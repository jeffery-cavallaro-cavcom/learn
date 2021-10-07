-include ~/make/cpp.mak

SIMPLE_PROGRAMS = limits convert literals

PROGRAMS = $(SIMPLE_PROGRAMS)

SOURCES =	limits.cc convert.cc literals.cc

all: $(PROGRAMS)

$(SIMPLE_PROGRAMS): %: %.cc
	$(LINK.o) $(OUTPUT_OPTION) $<

lint:
	@$(LINT.cc) $(INCLUDES) $(SOURCES)

clean:
	@${RM} -f $(LIBRARIES) $(PROGRAMS) $(OBJS)

distclean: clean
	@${RM} -f *.d

include $(TEMPLATES)/util.mak
