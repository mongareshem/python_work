from pathlib import Path

contents = 'I love programming\n'
contents += 'I love creating new games\n'
contents += 'I love working with data\n'
contents += 'I also love developing web apps'

path = Path('programming.txt')
path.write_text(contents)