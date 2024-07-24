#password checker: 
# if we don't show the user password, then we can use *. 
# if user password is 10 character length, then we just write as *10. 

name = input('name ?')
password = input('password?')

print(name)

print(password)

print(f'{name} you\'re password is {password} and it\'s {len(password)} letters long')

print((name) + ' your\'re password is ' + str(password) + ' and it\'s ' + str(len(password)) +' letters long')

# To make more clean code-- new variable for password length, and use it in code.

name = input('name ?')
password = input('password?')
password_length =len(password)

print(name)  
print(password)
print(f'{name} you\'re password is {password} and it\'s {password_length} letters long')

# if we don't show the password, use * 

name = input('name ?')
password = input('password?')

password_length = len(password)
password_secret = '*' * password_length

print(name)

print(password)

print(f'{name} you\'re password is {password_secret} and it\'s {password_length} letters long')

# if we want show specific characters. 
name = input('name ?')
password = input('password?')
password_length = len(password)

password_secret = ('**' + {password[2]} + '*' * {password_length - 3})

print(name)
print(password)
print(f'{name} you\'re password is {password_secret} and it\'s {password_length} letters long')