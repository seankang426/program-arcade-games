num = int(input('Enter a number: '))
spce = (num + 2) - 2
print('o' * ((num) * 2))
for i in range(1, num - 1):
    print('o' + (' ' * spce) + 'o')
print('o' + ((num) + 2))    
