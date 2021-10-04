# Other target rules.  This file should be included at the end of the Makefile.

help:
	@${MAKE} --print-data-base --question all | \
	$(GREP) -v -e '[Mm]akefile' -e '^[#.-]' | \
	$(GREP) -e '^[-A-Za-z0-9_]*\(.a\)*:' | \
	$(AWK) '/.*:/ { print substr($$1,1,length($$1)-1) }' | \
	$(SORT) | \
	$(PR) --omit-pagination --width=80 --columns=4

%.d: %.cc
	@$(CXX) $(CXXFLAGS) -M $< | sed 's/\($*\)\.o[ :]*/\1.o $@ : /g' > $@

-include $(subst .cc,.d,$(SOURCES))
