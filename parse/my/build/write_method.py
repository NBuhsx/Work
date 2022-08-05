import json
from typing import Generator, List
from pathlib import Path


from openpyxl import Workbook
from .help import ColumName


def write_json(
    pathfile:str|Path,
    trObj:Generator[List[str], None, None], 
    ensure_ascii:bool=False, 
    indent:int=3) -> None:

    with open(file=pathfile, mode='w', encoding='utf-8') as file:
        json.dump(
            obj=[ColumName.get_dict(*row) for row in trObj], 
            fp=file, 
            ensure_ascii=ensure_ascii, 
            indent=indent)


def write_cvs(pathfile:str|Path, trObj:Generator[List[str], None, None]):
    wb = Workbook()
    ws = wb.create_sheet(index=0)

    for row in (ColumName.get_tuple(), *trObj):
        ws.append(row)
    wb.remove(wb['Sheet'])
    wb.save(filename=pathfile)




