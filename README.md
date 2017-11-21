# Salários da Câmara Municipal de São Paulo (CMSP)

Este repositório contém um scraper para extrair os dados da remuneração dos
servidores efetivos e comissionados da Câmara Municipal de São Paulo. Os dados
estão disponíveis no site da [CMSP][cmsp-remuneracao], e você pode encontrar os
dados já extraídos usando esse scraper no arquivo [data/remuneration.csv][data].

## Atualizando os dados

Para atualizar os dados, você precisa ter Python 3.5+ e o [tox][tox] instalado.
Depois de instalá-los, basta você clonar esse repositório e executar `make
clean && make install` na linha de comando.

[tox]: https://tox.readthedocs.io/en/latest/
[cmsp-remuneracao]: http://www.camara.sp.gov.br/transparencia/salarios-abertos/remuneracao-dos-servidores-e-comissionados/
[data]: data/remuneration.csv
[datapackage]: datapackage.json
