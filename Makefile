PYTHON=python3
APP=main.py
STDDEV=stddev.py
PACKAGE=projekt.zip

.PHONY: all run clean pack test doc stddev help

all: run

run:
	$(PYTHON) $(APP)

stddev:
	$(PYTHON) $(STDDEV) 1 2 3 4 5

test:
	$(PYTHON) -m unittest discover -v

doc:
	@echo "Dokumentacia nie je implementovana"

clean:
	rm -f *.pyc
	rm -rf __pycache__
	rm -f $(PACKAGE)

pack:
	zip -r $(PACKAGE) . -x "*.git*" "__pycache__/*"

help:
	@echo "Pouzitie:"
	@echo " make run     - spusti kalkulacku"
	@echo " make stddev  - vypocita smerodajnu odchylku"
	@echo " make test    - spusti testy"
	@echo " make clean   - vymaze docasne subory"
	@echo " make pack    - vytvori zip"
