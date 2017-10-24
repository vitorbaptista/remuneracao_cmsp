salarios.json:
	scrapy crawl salarios_camara_sp -o salarios.json

clean:
	rm -f salarios.json
