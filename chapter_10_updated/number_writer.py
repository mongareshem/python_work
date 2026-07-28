from pathlib import Path
import json

numbers = [2, 3, 4, 8, 7, 9]
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)