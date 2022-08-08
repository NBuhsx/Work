
from pathlib import Path
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


DIR_PROJECT = Path(__file__).resolve().parent
RESULT_JSON = Path(DIR_PROJECT, 'result')


class Config(BaseModel):
    data_from: str = Field(
        default='01.1993',
        description="Дата начала отсчёта")
    data_to: str = Field(
        default=datetime.now().strftime("%m.%Y"),
        description="Дата окончания отсчёта")
    method_write: Literal['json', 'csv', 'all'] = Field(
        default='json',
        description="Метод записи"
    )
    

