str1 ="this is a string"
str2 ='ansh'
str3 = '''Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development'''

print(all([str1.islower(),str2.islower(),str3.islower()]))  


# print in next line using \n \t for tab space and \b for backspace 
# \r for carriage return and \f for form feed and \v for vertical tab
# \a for alert and \0 for null character

str1 = "this is a string.\nThis is a new line"
print(str1)


# concatination = joining two strings

str1 = "this is a string"
str2 = "this is another string"
str3 = str1 + str2
print(str3)

# Repetition of string

str1 = "this is a string"
str2 = str1 * 3
print(str2)

# Slicing of string

str1 = "this is a string"
print(str1[0:5]) # this
print(str1[5:]) # is a string
print(str1[:5]) # this
print(str1[:]) # this is a string
print(str1[0:5:2]) # ti
print(str1[::2]) # ti sasrn
print(str1[::-1]) # gnirts a si siht

# Membership of string

str1 = "this is a string"
print('this' in str1) # True
print('this' not in str1) # False

# Built-in functions

str1 = "this is a string"
print(len(str1)) # 16
print(max(str1)) # t
print(min(str1)) # " "

# Built-in methods

str1 = "this is a string"
print(str1.capitalize()) # This is a string
print(str1.upper()) # THIS IS A STRING
print(str1.lower()) # this is a string
print(str1.title()) # This Is A String
print(str1.swapcase()) # THIS IS A STRING
print(str1.center(50)) # "                this is a string                "
print(str1.count('i')) # 3
print(str1.find('i')) # 2
print(str1.index('i')) # 2
print(str1.replace('is','are')) # thare are a string
print(str1.split()) # ['this', 'is', 'a', 'string']
print(str1.split('i')) # ['th', 's ', 's a str', 'ng']
print(str1.strip()) # this is a string
print(str1.lstrip()) # this is a string
print(str1.rstrip()) # this is a string
print(str1.startswith('this')) # True
print(str1.endswith('string')) # True
print(str1.isalnum()) # False
print(str1.isalpha()) # False
print(str1.isdigit()) # False
print(str1.islower()) # True
print(str1.isupper()) # False
print(str1.isspace()) # False
print(str1.istitle()) # False
print(str1.join('123')) # 1this is a string2this is a string3
print(str1.partition('is')) # ('th', 'is', ' is a string')
print(str1.rpartition('is')) # ('this ', 'is', ' a string')
print(str1.rfind('i')) # 15
print(str1.rindex('i')) # 15
print(str1.rjust(50)) # "                                 this is a string"
print(str1.rsplit()) # ['this', 'is', 'a', 'string']
print(str1.splitlines()) # ['this is a string']
print(str1.zfill(50)) #


# indexing = 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

str ="Gautam Ansh"
str[2] 
str[0]
str[-1]
str[-2]
print( str, str[2],str[0],str[-1],str[-2])


