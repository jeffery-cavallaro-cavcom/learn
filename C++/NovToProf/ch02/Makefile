-include ~/make/cpp.mak

SIMPLE_PROGRAMS = types \
                  euclid \
                  inches \
                  infinity \
                  format \
                  yards \
                  circle \
                  tree \
                  bmi

PROGRAMS = $(SIMPLE_PROGRAMS)

SOURCES = types.cc \
          euclid.cc \
          inches.cc \
          infinity.cc \
          format.cc \
          yards.cc \
          circle.cc \
          tree.cc \
          bmi.cc

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
