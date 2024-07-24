#modules --> how to organize the code ! 
#as we write more lines of code, it gets harder and harder to keep everything in your head. 
#need an easy way to organize the code. 
#if we have multiple files in phyton because our project become bigger and bigger --> is there a way to link all these files together?
#the way of orginizing the code --> MODULES
#modules are simply each file in phyton
#each .py file is MODULE. 

#what if we have more files? Each file here is MODULE. 

# example: 
# working at Netflix --> a file -- dedicated to videos, another file or MODULE dedicated to login, another file --> for reccomendation
# we want to group these classes and functions together inside of a file.

# Let say: we have these functions in modules. py file. But we want to use these functions in modulexercise.py file. In moduleexercise file we will import this file into it.
# to communicate between these files : EASY : import (file name)

#let's we define new functions here: But we wnat to use these functions in moduleexercise.py file. GO TO moduleexercise.py file to call these functions. 
def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2


