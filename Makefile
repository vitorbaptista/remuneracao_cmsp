data/remunerations.csv:
	mkdir -p data/
	scrapy crawl remunerations -o data/remunerations.csv

clean:
	rm -rf data/
