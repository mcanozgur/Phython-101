#parameters and arguments

#parameters: are used when the define a function
#def say_hello():             #in the function we created, in the bracklets, we can write many parameters. 
    #print('helooooooğğğğ')

def say_hello(name, emoji):   #This function is able to receive these parameters: name and emoji.
    print(f'hellooo {name} {emoji}')

#arguments:  are used when we call the function. function_name(arguments)

#positional arguments: function_name(name, emoji) --> these are positional. We call this function using positional arguments.
#ın this example, first argument should be name, the second should be emoji. 

say_hello('Melike', ':)') 
say_hello('Güven', ':(') 

#keyword arguments: do not worry about the position. we write the arguments w/ their keys which are define in the parameter part. 
#you can call the function using keyword arguments. 

say_hello(emoji = ':)', name = 'melike') #here we wirte the keywords --> for emojı and name 

#default parameters: parameters are determined default.
#when we call the function, no need to write arguments. It prints the default parameters
#But, you can change the default arguments by writing new arguments when we call the funtion 

def say_hi(name = 'MCÖ' , emoji = ':)'):   #these are default arguments
    print(f'hellooo {name} {emoji}')

say_hi()                 #it prints hello MCÖ :) as default
say_hi('melike', ':)')   #the default parameters can be cahnged w/ written new arguments

