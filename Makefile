.PHONY: clean

data/remunerations.csv:
	mkdir -p data/
	tox -e run -- -o data/remunerations.csv

clean:
	rm -rf data/
