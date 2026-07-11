# import pizza #Imports ALL functions (everything) -> module.function()
# pizza.make_pizza(16, 'mushrooms', 'pepperoni', 'olives')

# from pizza import make_pizza #Imports SPECIFIC function(s); separate by a comma
# make_pizza(16, 'mushrooms', 'pepperoni', 'olives')

# from pizza import make_pizza as mp #Using aliases for functions
# mp(16, 'mushrooms', 'pepperoni', 'olives')

# import pizza as p #Using aliases for modules
# p.make_pizza(16, 'mushrooms', 'pepperoni', 'olives')

from pizza import * #Imports all functions (Not recommended for large modules)
make_pizza(16, 'mushrooms', 'pepperoni', 'olives')