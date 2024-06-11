def addItem(item): 
"""    Takes item and appends it to cart """ 
# append item to cart 
# print item is added
def removeItem(item): 
"""  Takes item and removes it from the cart """ 
# check if the item is in the list 
# if item is in list remove it with the remove operation.  Print item removed 
# otherwise, print item could not be removed
def showCart(): 
"""  Prints items in cart """ 
# check if there are items in the cart. 
# If it’s empty, let the user know. 
# Otherwise, loop over the items and output one per line.
def clearCart(): 
""" 
Clears items from cart and prints that cart is empty 
""" 
# Use clear() method to empty cart   
# Print cart is empty
def main(): 
done = False 
while not done: 
         ans = input('quit/add/remove/show/clear: ').lower()         
         if ans == 'quit': 
              print('Thanks for using our program.') 
              showCart()     # write this function  
              done = True 
         elif ans == 'add': 
              item = input('What would you like to add? ').title() 
              addItem(item)     # write this function  
         elif ans == 'remove': 
              showCart() 
              item = input('What item would you like to remove? ').title() 
              removeItem(item)   # write this function 
         elif ans == 'show': 
              showCart()     
         elif ans == 'clear': 
              clearCart()  #write this function  
         else: 
             print('Sorry that was not an option.') 
 
main()       # run the program
