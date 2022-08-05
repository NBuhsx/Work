import requests
from bs4 import BeautifulSoup

from datetime import datetime
from typing import Generator, List

from datetime import datetime



def parse_table_in_data(
    data_from:str|datetime=datetime.strptime('01.1993', "%m.%Y"),
    data_to:str|datetime=datetime.now().strftime("%m.%Y")) -> str:
    """:data_from and data_to accepts datatime format 'month.year' or string for example '01.2001'"""
    response = requests.get(
        'https://cbr.ru/hd_base/mrrf/mrrf_m',
        params={
            'UniDbQuery.Posted': True,
            'UniDbQuery.From': str(data_from),
            'UniDbQuery.To': str(data_to)
        })
    response.raise_for_status()
    return response.text



def return_tr(context:str) -> Generator[List[str], None, None]:
    page = BeautifulSoup(context, 'html.parser')
    table = page.find('table', class_='data spaced')
    for row in table.find_all('tr')[3:]:
        yield [
            value.get_text() for value in row.contents if value != '\n'
        ]
