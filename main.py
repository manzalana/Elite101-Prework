
'''
Welcome the user
Collect the user’s name and age
Ask the user how it can help them
Allow the user to choose from a menu/list of options on how they can continue the conversation


'''
convo_choices=['This is a response to option 1', 'This is a response to option 2', 'Goodbye, I hope you have a good day!']
active=True

print('Hello User!')
name=input('What is your name? ')
age=input('How old are you? ')
print(f"How can I assist you today, {name}?")



response=''
while active:
  choice=input('This will be a menu\n1. option one\n2. option two\n3. Exit program  ')
  if choice=='1':
    response=convo_choices[0]
  elif choice=='2':
    response=convo_choices[1]
  elif choice=='3':
    response=convo_choices[2]
    active=False
  else:
    response='Im sorry, I dont understand :('
  print(response)

