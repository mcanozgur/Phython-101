# string --> stands for string.

# to write a string, we need to use "".

print(type('melike'))     #print str.


# for long string or more than one line !  --> ''' is used. 

three_longstring = '''
güven
melike
robin
:) 
'''
print(three_longstring)

#string concatanation : to merge the all strings.

print ('melike' + ' ' + 'güven')                          # ' ' for space. you can also write -- print('melike ' + 'güven')
                                                                                                             #this space also supply a space before güven. 

print ('melike is' + ' ' + '30' + ' years old')           # normally, no need to use '' for integer. If we dont use int, then need to use ''. 

print ('melike is' + ' ' + str(30) + ' years old')        # Here, usage of integer, but we want to write a string, so we need to change it to str().


