import time

time.sleep(2)
# intro
print(
	'\nWelcome to the new Coffee machine! My name is  " Beniko "\n"Balanced, Enhancing, Natural, Interactive, Kind, and Optimized"\nand i am a friendly Artificial barista! :)')
coffee_options = ['Espresso', 'Cappuccino', 'Latte', 'Americano']

coffee_beans = ['Arabica', 'Robusta', '60 40']

milk_options = ['Whole Milk', 'Almond Milk', 'Soy Milk', 'Nothing']

flavorings = ['Vanilla', 'Caramel', 'Hazelnut', 'Mocha', 'Nothing']

sizes = ['Small', 'Medium', 'Large']

prep_times = [10, 25, 30, 26]  # Every prep time is different based on the coffee type!

time.sleep(5.5)

input('[Enter] to continue')  # Of course , input!
# Name of the user
name = input('''----------------------------------
So , What should i call you? ''')

if not name:  # if The User's name is invalid , Beniko will call them 'No one'
	name = 'No one'

for i, option in enumerate(coffee_options):  # Coffee options
	print(f'{i + 1}. {option}')
# Order or Choices
choice = int(input('''
----------------------------------
Alright ,Which coffee would you like to order? '''))
print(f'Ok, {coffee_options[choice - 1]}')
# Advanced adjustment like Coffee bean or type of milk etc.
advanced = input('''----------------------------------
Do you want advanced adjustments (yup/nope)? 
''')
if advanced.lower() == 'yup':
	print('''----------------------------------
Ok! Here are our coffee bean options:
    ''')
	for i, option in enumerate(coffee_beans):
		print(f'{i + 1}. {option}')
	bean_choice = int(input('''
----------------------------------
Which type of coffee beans would you like? I recommend "60 40" 
but you can choose whatever you want! '''))
	print(f'Ok, {coffee_beans[bean_choice - 1]}')
	print('''----------------------------------
Here are our milk options:
''')
	for i, option in enumerate(milk_options):
		print(f'{i + 1}. {option}')
	milk_choice = int(input('''
----------------------------------
Which type of milk would you like? '''))
	print(f'Me Love {milk_options[milk_choice - 1]}!')
	print('''----------------------------------
Here are our delicious flavoring options:
''')
	for i, option in enumerate(flavorings):
		print(f'{i + 1}. {option}')
	flavor_choice = int(input('''
----------------------------------
Which flavoring would you like? '''))
	print('Roger that')

print('''----------------------------------
Here are our size options:
''')
for i, option in enumerate(sizes):
	print(f'{i + 1}. {option}')
size_choice = int(input('''
----------------------------------
Which size would you like? '''))
print(f'Ok, {sizes[size_choice - 1]}')
# And here is extra shots of espresso option for when you want to get the full energy
extra_shots = int(input('''----------------------------------
How many extra shots of espresso would you like (0-2)? '''))
sugar = -1  # Amount of everything before choosing
coffee = -1
milk = -1

while sugar < 0 or sugar > 5 or coffee < 0 or coffee > 5 or milk < 0 or milk > 5:  # Keep looping until the user enters valid values for sugar, coffee, and milk.
	if sugar < 0 or sugar > 5:
		sugar = int(input("How many teaspoons of sugar would you like (0-5)? "))
	if coffee < 0 or coffee > 5:
		coffee = int(input("How many shots of coffee would you like (0-5)? "))
	if milk < 0 or milk > 5:
		milk = int(input("How many ounces of milk would you like (0-5)? "))
	if sugar == 0 and coffee == 0 and milk == 0:
		print(f"You haven't selected anything, {name}. Let's try again!")
		sugar = -1
		coffee = -1
		milk = -1
print(
	f"Preparing your {sugar} teaspoons of sugar, {coffee} shots of coffee, and {milk} ounces of milk...")  # Print a message confirming the order.
time.sleep(4)  # Sleep for a few seconds to simulate the time it takes to make the coffee.
print(f"Your coffee is ready, {name}!")  # Print a message that the coffee is ready.
if sugar > 2:
	print(
		f"Thank you for your purchase! Enjoy your really sweet cup of coffee!")  # Check if the user ordered a sweet coffee.
elif coffee > 3:
	print(f"Wow, {name}! You have a lot of caffeine in your coffee!")  # Check if the user ordered a strong coffee.
elif milk > 0 and coffee_options[choice - 1] in ['Espresso','Americano']:  # Check if the user ordered a coffee with milk.
	print(f"Are you sure you're old enough to drink coffee? Enjoy your coffee with milk!")
elif milk == 0 and coffee_options[choice - 1] in ['Latte','Cappuccino']:  # Check if the user ordered latte or cappuccino without milk.
	print(f"We'll add some milk for you. It's delicious in a coffee!")

else:  # Otherwise, the coffee is just right.
	print(f"Thank you for your purchase! Enjoy your delicious coffee!")

feedback = input("What were your thoughts on this program? ")  # Get the user's feedback.

# Write the feedback to a file. not important I just used it to anyone who used this program , the feedback get saved, so I can review it later!
with open("feedback.txt", "a") as f:
	f.write(f"{feedback}\n")
print(f"Thank you for your feedback, {name}! Have a nice day!")  # Thank the user for their feedback.
