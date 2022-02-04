

# Get the input from the user.
message = input('What would you like the cat to say? ')

# Determine the length of the input.
messageLen = len(message)


# Make the bubble the same size as the input.
print((' ' * 12) + ('_' * messageLen))
print((' ' * 10) + '< ' + message + ' >')
print((' ' * 12) + ('-' * messageLen))
print((' ' * 10) + '/')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')



print('            ' + ('_' * messageLen))
print('          < ' + message + ' >')
print('            ' + ('-' * messageLen))
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')



print('            {}'.format('_' * messageLen))
print('          < {} >'.format(message))
print('            {}'.format('-' * messageLen))
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')
