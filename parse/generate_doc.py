from my.config import Config
from pathlib import Path
from json_schema_for_humans.generate import generate_from_filename



DIR = Path(Path(__file__).resolve().parent, 'schema')




def generate_html():
    with open(Path(DIR, 'SchemaConfig.json'), mode='w') as file:
        file.write(Config.schema_json(indent=2))
    generate_from_filename(
        schema_file_name=Path(DIR, 'SchemaConfig.json'), 
        result_file_name=str(Path(DIR, 'schema_doc.html')))

def generate_md():
    with open(Path(DIR, 'SchemaConfig.json'), mode='w') as file:
        file.write(Config.schema_json(indent=2))
    generate_from_filename(
        schema_file_name=Path(DIR, 'SchemaConfig.json'), 
        result_file_name=str(Path(DIR, 'schema_doc.md')), 
        copy_js=False,
        copy_css=False)


if __name__ == "__main__":
    generate_html()
    generate_md()