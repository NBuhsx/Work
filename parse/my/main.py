from pydantic import parse_file_as
from pathlib import Path
from datetime import datetime



from build.request_and_bs import parse_table_in_data, return_tr
from build.write_method import write_json, write_cvs
from config import RESULT_JSON, DIR_PROJECT, Config



def main():
    config = parse_file_as(Config, path=Path(DIR_PROJECT, 'config.json'))
    match config.method_write:
        case "json":
            write_json(
                pathfile=Path(RESULT_JSON, f'cdr_{datetime.now().strftime("%d-%m-%Y_%H-%M")}.{config.method_write}'), 
                trObj=return_tr(
                parse_table_in_data(
                    data_from=config.data_from,
                    data_to=config.data_to)))
        case "csv":
            write_cvs(
                pathfile=Path(RESULT_JSON, f'cdr_{datetime.now().strftime("%d-%m-%Y_%H-%M")}.{config.method_write}'), 
                trObj=return_tr(
                    parse_table_in_data(
                        data_from=config.data_from,
                        data_to=config.data_to)))
        case _:
            print("Не понятный метод записи")
   
    
 
if __name__ == "__main__":
    main()
