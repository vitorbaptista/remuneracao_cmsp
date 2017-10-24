import scrapy
import re


class CamaraSp(scrapy.Spider):
    name = 'salarios_camara_sp'
    start_urls = [
        'http://www.camara.sp.gov.br/wp-content/uploads/salariosabertos/HTML_ativos_2017_09/todos.html',
    ]

    def parse(self, response):
        current_lotacao = None
        date_of_reference = self._parse_date_of_reference(response)
        for row in response.css('#tabela_principal tr'):
            if self._is_lotacao_row(row):
                current_lotacao = row.css('.lin_lotacao::text').extract_first().strip()
            elif self._is_person_row(row):
                yield self._parse_person_row(row, current_lotacao, date_of_reference)

        pass

    def _is_lotacao_row(self, row):
        return bool(row.css('.lin_lotacao'))

    def _is_person_row(self, row):
        return bool(row.css('.nome_valor'))

    def _parse_date_of_reference(self, response):
        title = response.css('#titulo_da_pagina::text').extract_first()
        if not title:
            return

        matches = re.search('referente a (\d+)\/(\d+)', title)
        if matches:
            month, year = matches.groups()
            return {
                'month': int(month),
                'year': int(year),
            }

    def _parse_person_row(self, row, lotacao, date_of_reference):
        person = {
            'nome': row.css('.nome_valor::text').extract_first().strip(),
            'cargo': row.css('.cargo_valor::text').extract_first().strip(),
            'funcao': row.css('.funcao_valor::text').extract_first().strip(),
            'remuneracao': self._parse_salary(row.css('.remun_valor')),
            'lotacao': lotacao,
        }

        if date_of_reference:
            person['ano'] = date_of_reference['year']
            person['mes'] = date_of_reference['month']

        if person['cargo'] != '-':
            return person

    def _parse_salary(self, row):
        if bool(row.css('.remun_unica')):
            salary = row.css('.remun_unica a::text').extract_first()
        else:
            salary = row.css('tr:last_child .remun_dir a::text').extract_first()

        if salary:
            return self._currency_str_to_float(salary.strip())

    def _currency_str_to_float(self, currency):
        clean_number_str = currency.replace('R$ ', '') \
            .replace('.', '') \
            .replace(',', '.')

        return float(clean_number_str)
