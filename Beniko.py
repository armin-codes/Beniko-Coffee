import time

time.sleep(5)

print('''

Welcome to the new Coffee machine! My name is  " Beniko "

"Balanced, Enhancing, Natural, Interactive, Kind, and Optimized"

and i'm a friendly Artificial barista! :)
''')
coffee_options = ['Espresso', 'Cappuccino', 'Latte', 'Americano']
coffee_beans = ['Arabica', 'Robusta', '60 40']
milk_options = ['Whole Milk', 'Almond Milk', 'Soy Milk', 'Nothing']
flavorings = ['Vanilla', 'Caramel', 'Hazelnut', 'Mocha', 'Nothing']
sizes = ['Small', 'Medium', 'Large']
prep_times = [10, 25, 30, 26]

time.sleep(5.5)
input('[Enter] to continue')
name = input('''----------------------------------
So , What should i call you? ''')
if not name:
    name = 'No one'
for i, option in enumerate(coffee_options):
    print(f'{i+1}. {option}')
choice =int(input('''
----------------------------------
Alright ,Which coffee would you like to order? '''))
print(f'Ok, {coffee_options[choice-1]}')
advanced = input('''----------------------------------
Do you want advanced adjustments (yup/nope)? 
''')
if advanced.lower() == 'yup':
    print('''----------------------------------
Ok! Here are our coffee bean options:
    ''')
    for i, option in enumerate(coffee_beans):
        print(f'{i+1}. {option}')
    bean_choice = int(input('''
----------------------------------
Which type of coffee beans would you like? I recommend "60 40" 
but you can choose whatever you want! '''))
    print(f'Ok, {coffee_beans[bean_choice-1]}')
    print('''----------------------------------
Here are our milk options:
''')
    for i, option in enumerate(milk_options):
        print(f'{i+1}. {option}')
    milk_choice = int(input('''
----------------------------------
Which type of milk would you like? '''))
    print(f'Me Love {milk_options[milk_choice-1]}!')
    print('''----------------------------------
Here are our delicious flavoring options:
''')
    for i, option in enumerate(flavorings):
        print(f'{i+1}. {option}')
    flavor_choice = int(input('''
----------------------------------
Which flavoring would you like? '''))
    print('Roger that')

print('''----------------------------------
Here are our size options:
''')
for i, option in enumerate(sizes):
    print(f'{i+1}. {option}')
size_choice = int(input('''
----------------------------------
Which size would you like? '''))
print(f'Ok, {sizes[size_choice-1]}')

extra_shots = int(input('''----------------------------------
How many extra shots of espresso would you like (0-2)? '''))

sugar = -1
coffee = -1
milk = -1
while sugar < 0 or sugar > 5 or coffee < 0 or coffee > 5 or milk < 0 or milk > 5:
    if sugar < 0 or sugar > 5:
        sugar = int(input('''----------------------------------
How many teaspoons of sugar would you like (0-5)? '''))
    if coffee < 0 or coffee > 5:
        coffee = int(input('''----------------------------------
How many shots of coffee would you like (0-5)? '''))
    if milk < 0 or milk > 5:
        milk = int(input('''----------------------------------
How many ounces of milk would you like (0-5)? '''))
    if sugar == 0 and coffee == 0 and milk == 0:
        print(f"""----------------------------------
You haven\'t selected anything, {name}. Let's try again!""")
        sugar = -1
        coffee = -1
        milk = -1

if sugar == 5 and coffee == 5 and milk == 5:
    print(f'''Woah, you're going all in, aren't you?''')

print(f'''----------------------------------

Preparing your {sizes[size_choice-1]} {coffee_options[choice-1]}...
''')
time.sleep(prep_times[choice-1])
print(f'''----------------------------------
{name} ,Your {sizes[size_choice-1]} {coffee_options[choice-1]} is ready!''')

if sugar > 2:
    print(f'''----------------------------------
Thank you for your purchase! Enjoy your really sweet cup of {sizes[size_choice-1]} {coffee_options[choice-1]}''')
elif coffee > 3:
    print(f'Wow, {name}! You have a lot of caffeine in your  {coffee_options[choice-1]}!')
elif (milk > 0) and (coffee_options[choice-1] in ['Espresso', 'Americano']):
    print(f'Are you sure you\'re old enough to drink coffee? Enjoy your {sizes[size_choice-1]} {coffee_options[choice-1]} with milk!')
elif (milk == 0) and (coffee_options[choice-1] in ['Latte', 'Cappuccino']):
    print(f'We\'ll add some milk for you. It\'s delicious in a {sizes[size_choice-1]} {coffee_options[choice-1]}')
elif coffee == 0:
    print(f'Umm, we\'ll add a bit of coffee for you. It wouldn\'t be coffee without it!')
else:
    print(f'Thank you for your purchase! Enjoy your delicious cup of {sizes[size_choice-1]} {coffee_options[choice-1]}!')
feedback = input('''----------------------------------
What were your thoughts on this program? ''')

with open('feedback.txt', 'a') as f:
    f.write(feedback + '\n')

print(f'Thank you for your feedback, {name}! Have a nice cup of coffee!')
