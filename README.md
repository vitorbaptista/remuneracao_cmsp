# Remunerations of the São Paulo Civil Council's public servants

This repository contains a scraper that extracts the remuneration data from
the [São Paulo's Civil Council website][cmsp-remuneracao]. You can find the data
already extracted on [data/remuneration.csv][data].

This repository is also a [Data Package][datapackage], so you can use any tools that
support the specification.

## Using

### Requirements

The only requirements to run this code is Python 3.6 and [tox][tox] (it'll probably run
with earlier version of Python, but I haven't tested it).

### Updating the data

To update the data, open your command-line and run:

```
make clean
make
```

### Validating the data

We use [goodtables][goodtables] to validate that the data we extract conforms to the schema
we defined in the [datapackage.json](datapackage.json) file. To execute the tests, simply run
`tox`.

[tox]: https://tox.readthedocs.io/en/latest/
[cmsp-remuneracao]: http://www.camara.sp.gov.br/transparencia/salarios-abertos/remuneracao-dos-servidores-e-comissionados/
[data]: data/remuneration.csv
[datapackage]: https://frictionlessdata.io/data-packages/
[goodtables]: https://github.com/frictionlessdata/goodtables-py/
