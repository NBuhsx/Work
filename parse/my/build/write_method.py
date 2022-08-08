import json
from typing import Generator, List, Iterator
from pathlib import Path

import csv
from .help import ColumName


def write_json(
    pathfile:str|Path,
    trObj:Generator[List[str], None, None]|Iterator[List[str]], 
    ensure_ascii:bool=False, 
    indent:int=3) -> None:

    with open(file=pathfile, mode='w', encoding='utf-8') as file:
        json.dump(
            obj=[ColumName.as_dict(*row) for row in trObj], 
            fp=file, 
            ensure_ascii=ensure_ascii, 
            indent=indent)


def write_cvs(pathfile:str|Path, trObj:Iterator[List[str]]|Generator[List[str], None, None]):
    with open(file=pathfile, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(ColumName.as_title())
        writer.writerows(trObj)





