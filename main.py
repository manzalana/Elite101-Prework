
'''
Welcome the user
Collect the user’s name and age
Ask the user how it can help them
Allow the user to choose from a menu/list of options on how they can continue the conversation


'''

active=True

print('Hello User!')
name=input('What is your name? ')
age=input('How old are you? ')
print(f"How can I assist you today, {name}?")

convo_choices=[f"Cool, I can help you with any math you need, {name}!", 'Alright! How has your day been so far?', 'Goodbye, I hope you have a good day!']


response=''
while active:
  choice=input('\nPlease enter a number from the menu below\n1. Math Help\n2. Do you just want to chat?\n3. Exit program  \n')
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

