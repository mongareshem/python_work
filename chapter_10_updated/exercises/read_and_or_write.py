from pathlib import Path
import json

path = Path('number.json')

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f'I know your favorite number, it is {number}!')
else:
    number = input("What is your number? ")
    content = json.dumps(number)
    path.write_text(content)