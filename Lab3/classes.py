import math

class NewClass:
    def __init__(self):
        self.string =""
    def GetString(self):
        self.string = input()
    def upper(self):
        print(self.string.upper())



class shape:
    def __init__(self) -> None:
        self.area = -1
    def area1(self):
        print(self.area)

class square(shape):
    def __init__(self,leng) -> None:
        self.area = leng*leng
        self.length = leng

class rectangle(shape):
    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width
        self.area = length*width

class point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def move_by(self,x,y):
        self.x+=x
        self.y+=y
    def move_to(self,x,y):
        self.x=x
        self.y=y
    def dist(self,point2):
        return ((self.x-point2.x)**2+(self.y-point2.y)**2)**0.5

class Account:
    def __init__(self,owner,balance) -> None:
        self.owner = owner
        self.balance = balance
    def deposit(self,money):
        self.balance+=money
    def withdraw(self,money):
        if self.balance>=money:
            self.balance-=money
        else:
            print(f"you don't have enough money({self.balance-money})")      

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


prime_numbers = list(filter(lambda x: prime(x), numbers))


print("Prime numbers:", prime_numbers)