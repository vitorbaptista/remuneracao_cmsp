data/salarios.csv:
	mkdir -p data/
	scrapy crawl salarios_camara_sp -o data/salarios.csv

clean:
	rm -rf data/
