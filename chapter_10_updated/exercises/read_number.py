from pathlib import Path
import json

path = Path('number.json')
content = path.read_text()
number = json.loads(content)

print(f'I know your favorite number, it is {number}!')