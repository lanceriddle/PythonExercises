

message = input('What would you like the cat to say? ')
messageLen = len(message)


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
