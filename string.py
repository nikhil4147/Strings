x = "hello"
y = 'Hello'
print(type(x))
print(type(y))
print(len(x))
print(x)
print(y)


#Slicing
#You can return a range of characters by using the slice syntax.

#Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])


#Slice From the Start

b = "Hello World"
print(b[ :4])


#Slice To the End

b = "Hello World"
print(b[1:])

#Negative Indexing

b = "Hello World"
print(b[-4:-1])


#Upper Case:

a = "python is a high level programming language"
print(a.upper())


#Lower Case:

a = "HELLO"
print(a.lower())

#Remove Whitespace:

x =   "Hello, World!"
print(x.strip())
