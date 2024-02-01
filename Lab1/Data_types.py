#Data types examples:
x=16
print(type(x))
#Data type
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"}) #frozenset	
x = True	#bool	
x = b"Hellooo" #bytes
x = bytearray(5) #bytearray
x = memoryview(bytes(5))	#memoryview	
x = None #NoneType
#Setting the specific data type
a = str("Hello World")
b = int(20)
c = float(20.5)
d = complex(1j)	
e = list(("apple", "banana", "cherry"))	
f = tuple(("apple", "banana", "cherry"))	
g = range(6)
h = dict(name="John", age=36)	
i = set(("apple", "banana", "cherry"))	
j = frozenset(("apple", "banana", "cherry"))	
k = bool(5)	
l = bytes(5)
m = bytearray(5)	
n = memoryview(bytes(5))
#Data types exercices
#1_st exercise
x = 49
print(type(x))
#2_nd exercise
y = "Hello World"
print(type(y))
#3_rd exercise
z = 20.5
print(type(z))
#4_th exercise
c = ["apple", "banana", "cherry"]
print(type(c))
#5_th exercise
d = ("apple", "banana", "cherry")
print(type(d))
#6_th exercise
f = {"name" : "John", "age" : 48}
print(type(f))
#7_th exercise
b = True
print(type(b))