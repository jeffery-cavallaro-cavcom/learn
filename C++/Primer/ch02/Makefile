-include ~/make/cpp.mak

SIMPLE_PROGRAMS = limits

PROGRAMS = $(SIMPLE_PROGRAMS)

SOURCES =	limits.cc

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
