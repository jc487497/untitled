name = input('Enter your name: ')
while len(name) <= 1:
    print('Invalid name!')
    name = input ("Enter your name: ")
print("Welcome ", name)
