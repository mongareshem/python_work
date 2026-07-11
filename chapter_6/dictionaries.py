alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
print(f"You just earned {alien_0['points']} points!")

print()

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}.')

print()

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# alien_0['speed'] = 'fast' #This can be slow/fast/anything

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print(f'The new alien position is {alien_0["x_position"]}')

print()

alien_0 = {'color': 'green', 'points': 5,}
del alien_0['points']
print(alien_0)

print()

favorite_languages = {
    'shem': 'python',
    'lawrence': 'javascript',
    'david': 'flutter',
    'sarah': 'c',
}
print(f"Shem's favorite language is {favorite_languages['shem'].title()}")