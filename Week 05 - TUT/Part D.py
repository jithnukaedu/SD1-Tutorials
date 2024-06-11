#----------Example 1----------
name = "liz"
for char in name:
    print(char.upper()*3)

#----------Example 2----------
#Here we introduce a count to the loop and use ‘f-strings’ formatting.
message = "Testing"
count = 0
for character in message:
    print(f'Index:{count}, Character:{character}')
    count += 1
