import pyinputplus as pyip 

# Access the values of each input item, then assign a price to them. Add the price at the end depending on the choice

print('Please select which option as you go through the menu. Enter the word or number corresponding to the item')


bread_type = pyip.inputMenu(['white', 'wheat', 'sourdough'], numbered=True)  
protein_type = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True) 
cheese_yn = pyip.inputYesNo(prompt='Would you like cheese with that?')

if cheese_yn == 'yes':
	cheese_type = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)

topping_yn = pyip.inputYesNo(prompt='Would you like to choose 1 extra topping?')

if topping_yn == 'yes':
	topping_type = pyip.inputMenu([r'Mayo', 'Mustard', 'Lettuce', 'Tomato'], numbered=True)

amount_of_sandwiches = pyip.inputInt(prompt='How many sandwiches would you like? ')

total_price = 0 

if bread_type:
	total_price += 1

if protein_type:
	total_price += 3

if cheese_type:
	total_price += .75
else:
	pass

if topping_type:
	total_price += .5
else:
	pass	

print(f'Your order of {amount_of_sandwiches} {protein_type} {cheese_type} {topping_type} on {bread_type} is ready! The total price of the order is: £{amount_of_sandwiches * total_price}')
