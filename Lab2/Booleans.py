#Bool examples
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33
if b>a:
    print("b is bigger than a")
else:
    print("a is bigger than b")

print(bool("Hello"))
print(bool(15))

x,y  = "Help",15
print(bool(x),bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
print(isinstance(x, int))

#Exeerrrrrrciseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeessssssssss!!!!!!!!!!!!!
#1st
print(10>9)
#True

#2nd
print(10==9)
#False

#3rd
print(10<9)
#False

#4th
print(bool("abc"))
#True

#5th
print(bool(0))
#False