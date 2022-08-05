from my.config import Config
from pathlib import Path
from json_schema_for_humans.generate import generate_from_filename



DIR = Path(Path(__file__).resolve().parent, 'schema')

with open(Path(DIR, 'SchemaConfig.json'), mode='w') as file:
    file.write(Config.schema_json(indent=2))

generate_from_filename(Path(DIR, 'SchemaConfig.json'), Path(DIR, 'schema_doc.md'))