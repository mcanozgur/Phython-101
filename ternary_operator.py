#ternary operator: similar w/if else. it is a shortcut and used in certain logical conditions.
#to make cleaner code.
#conditional operation based on the condition -- true or not

#bunu tek satırda yazıyoruz. aslında if durumunu sağladığında print(') demek yerine başka bir variable ile if durumu 
#sağlandığında veya sağlanmadığında ne yazması gerektiğini

is_friend = True
can_message = 'messeage allowed' if is_friend else 'not allowed'

print(can_message) 

# Short Circuting: 
# when two conditions are linked w/ and statement, then first condition is not true, then the other statement is not checked --> this is short circuting
#AND Keyword : both statement will be checked.
is_Friend = True
is_user = True

print(is_Friend and is_user) #both statement is true, so TRUE will be printed. 

#OR keyword: 1 statement is enough to print TRUE.

is_Friend = True
is_user = True

if is_Friend or is_user:
    print('best friends forever')


#Logical Operator:
# < , > , == gibi şeyler
# == mean. equal to 
# >= ---> gretaer or equal -- OR condition
# <= ---> smaller or equal -- OR condition
# != ---> NOT EQUAL TO

print(1<2<3<4)   #Ture 
print(1 >= 0)    #True 
print(1 != 1)    #False 

#NOT keyword ---> used as FUNCTION and it means the OPPOSITE

print(not(False))  # True basar.
print(not(1 == 1)) #False

#exercise

is_magician = False
is_expert = True

#check if magician AND expert: print you are master magician
#if magician but not expert print at least you are getting there
#if your are not a magician: you need magic powers

if is_magician and is_expert:
    print('you are the master magician')
elif is_magician and not is_expert:
    print('you\'re getting there')
elif is_expert and not is_magician:
    print('you need magic powers')