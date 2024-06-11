def describe_pet(pet_name, animal_type='dog'): 
"""Display information about a pet.""" 
print("My " + animal_type + "'s name is " + pet_name + ".") 
#Test data to call the function 
describe_pet('Rover') 
describe_pet('Ginger', 'cat') 
describe_pet('Bobby', 'dog') 
