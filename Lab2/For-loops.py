#example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#example 2
for x in "banana":
  print(x)
  
#example 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#example 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
#example 5  
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  
#example 6
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    
#example 7
for x in [0, 1, 2]:
  pass
  
#example 8
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#example 9
for x in range(6):
  print(x)
  
#example 10
for x in range(2, 6):
  print(x)
  
#example 11
for x in range(2, 30, 3):
  print(x)
  
#example 12
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#FOR LOOPPOPOPOPOOP EXERZIZEEEZZZ
#1st
fruits = ['apple','banana','cherry']
for i in fruits:
  print(x)

#2nd
fruits = ['apple','banana','cherry']
for x in fruits:
  if x =='banana':
    continue
  print(x)

#3rd
for i in range(6):
  print(x)

#4th
fruits = ['apple','banana','cherry']
for x in fruits:
  if x == 'banana':
    break
  print(x)