# Given dictionary
tel = {'Andrea': 4351, 'Gill': 3506}

# A. Write the code to add ‘Ivan’ : 3483 to the dictionary. Then print the dictionary.
tel['Ivan'] = 3483
print(tel)

# B. Write the code to print the extension number for Andrea.
print(tel['Andrea'])

# C. Write the code to print all the keys used in the dictionary.
print(tel.keys())

# D. Replace the extension number for ‘Ivan’ with 4422. Then print the dictionary.
tel['Ivan'] = 4422
print(tel)

# E. What would happen if you try to access tel[‘Roy’]? 
#    What method could you use to return ‘None’ rather than produce an error?
# If you try to access tel['Roy'], it will raise a KeyError.
# You can use the get() method to return None if the key is not found.
print(tel.get('Roy'))

# F. Write the code to print all the values used in the dictionary.
print(tel.values())

# G. Write the code to check if the key ‘Andrea’ is in the dictionary. Print out the result.
print('Andrea' in tel)
