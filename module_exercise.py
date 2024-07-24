#modeulexercise.py

# import FILE NAME w/o py

import module_mc

print(module_mc)   #it will show storage area in memory.  

#this file also open a cache, this cache you can see imported functions. 

# ıf you aim is to apply the functions in module_mc; THEN --

import module_mc

print (module_mc.multiply(2,3))    
       #we use use dot after file name, we can show the available functions in this file to use.
print(module_mc.divide(5,2))

# packages in phyton

# mesela module_mc nin altına da file ekledin. Bu durumda module_mc artık PACKAGE. altındaki ise MODULE !
# import subfile_module_mc dediğimizde --> ERROR NO MODULE NAME as subfile module diyecek.
# import package name (yani module_mc). module name --> yazarak package içerisindeki module'ü çağırırız.
# print(package name . module name. function  ) --> ile istediğimiz function yaptırabiliriz.  

#DIFFERENT WAYS TO IMPORT
#we can have also another pacakge inside a package. 
#Bu durumda yine import kullanacağız : import(en üstteki package.altpackage.module.module içerisinden ne istersek o).
#Fakat if we have more and more package inside a package. this import process may be difficult.else
#Daha kolay olması için --> from packagename.packagename.module import whatever function we want.
                             #daha sonrasında print(function) --> print içerisine sadece istediğin functionı yazarsın. 
                            