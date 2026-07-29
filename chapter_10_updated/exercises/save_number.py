from pathlib import Path
import json

number = input("What is your number? ")
path = Path('number.json')
content = json.dumps(number)
path.write_text(content)