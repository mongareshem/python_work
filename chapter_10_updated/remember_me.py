from pathlib import Path
import json

name = input('What is your name? ')

path = Path('username.json')
contents = json.dumps(name)
path.write_text(contents)

print(f"We'll try to remember you when you come back, {name.title()}!")