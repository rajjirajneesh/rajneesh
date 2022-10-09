given_string = input('Enter a string: ')

even_chars = []
odd_chars = []
print('length of string=',len(given_string))
if(len(given_string)>7):
    for i in range(len(given_string)):
        if(i % 2 == 0):
            even_chars.append(given_string[i])
if(len(given_string)<=7):
    for i in range(len(given_string)):
        if(i % 2!=0):
            odd_chars.append(given_string[i])
            
print('Odd characters: {}'.format(odd_chars))
print('Even characters: {}'.format(even_chars))
                
            
            
            
    




