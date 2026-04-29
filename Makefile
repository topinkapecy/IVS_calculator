PYTHON=python3
APP=main.py
STDDEV=stddev
PACKAGE=projekt.zip

.PHONY: all run clean pack test doc stddev help profile install

all:
	@echo "Use 'make run' to start the calculator"

run:
	$(PYTHON) $(APP)

stddev:
	./$(STDDEV) 1 2 3 4 5

profile:
	$(PYTHON) -m cProfile -s tottime $(STDDEV) 1 2 3 4 5

test:
	$(PYTHON) -m unittest discover -v

doc:
	@echo "Dokumentacia nie je implementovana"

clean:
	rm -f *.pyc
	rm -rf __pycache__
	rm -f $(PACKAGE)

pack:
	zip -r $(PACKAGE) . -x "*.git*" "__pycache__/*" ".idea/*"

help:
	@echo "make run / stddev / profile / test / clean / pack"

install:
	mkdir -p $(DESTDIR)/usr/lib/ivs-calculator
	cp *.py $(DESTDIR)/usr/lib/ivs-calculator/
	cp -r math_ivs $(DESTDIR)/usr/lib/ivs-calculator/
	cp logo.png $(DESTDIR)/usr/lib/ivs-calculator/
	mkdir -p $(DESTDIR)/usr/bin
	printf '#!/bin/bash\ncd /usr/lib/ivs-calculator\npython3 /usr/lib/ivs-calculator/main.py "$$@"\n' \
		> $(DESTDIR)/usr/bin/ivs-calculator
	chmod +x $(DESTDIR)/usr/bin/ivs-calculator
