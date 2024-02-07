import math,random#,os
def OuncesToGrams(Ounces):
    return Ounces*28.3495231
# print(OuncesToGrams(123))

print("###")

def Centigrade(Farenheit):
    return eval(f"(5 / 9) * ({Farenheit} - 32)")
# print(Centigrade(75))

print("###")

def solve(nheads,nlegs):
    nlegs /=2
    fleg = nlegs-nheads
    tleg = nheads-fleg
    print(f"rabbits:{fleg}, chickens:{tleg}")
# solve(3,8)

print("###")

def IsPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def filter_prime(numsstr):
    nums = map(int,numsstr.split())
    resw = []
    for num in nums:
        if IsPrime(num):
            resw.append(num)
    return resw
#print(filter_prime(input()))

print("###")
 
def rev(str):
    stra = str.split()
    res = ""
    for i in stra:
        res=i+" "+res
    return res
# print(rev(input()))

print("###")
 
def has_33(nums):
    t=1
    for i in nums:
        if t==i:
            return True
        t = i
    else:
        return False
print(has_33([3,3,3]))
# print(has_33([1,3,3]))
# print(has_33([3,1,3]))
# print(has_33([3,3,1]))
# print(has_33([3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3]))

print("###")
 
def spy_game_broken(nums,example = [0,0,7]):
    now = []
    nownotfull = True
    for i in nums:
        now.append(i)
        if nownotfull:
            now.append(i)
            nownotfull = False 
            continue
        if now==example:
            return True
        else:
            now.pop(0)
    return False

def spy_game(nums, example = [0,0,7]):
    now = []
    for i in nums:
        if i==example[len(now)]:
            now.append(i)
        if example==now:
            return True
    return False
def spy_game_v2(nums):    
    zero, zero1 ,seven = False, False, False
    for i in nums:
        if i ==0:
            if zero:
                zero1 = True
            else:
                zero = True
        if zero and zero1 and i == 7:
            seven  = True
        if zero and zero1 and seven:
            return True
    return False


# print(spy_game([1,2,4,0,0,7,5]) )
# print(spy_game([1,0,2,4,0,5,7]) )
# print(spy_game([1,7,2,0,4,5,0]) )

# print(spy_game_copy([1,2,4,0,0,7,5]) )
# print(spy_game_copy([1,0,2,4,0,5,7]) )
# print(spy_game_copy([1,7,2,0,4,5,0]) )

print("###")
 
def Volume_of_sphere(Radius):
    return "{:.2f}".format(eval(f"4/3*{math.pi}*{Radius**3}"))
print(Volume_of_sphere(4))

print("###")
 
def Delete_NonUnical(l):
    res = []
    for i in l:
        if i in res:
           continue
        res.append(i)
    return res

# print(Delete_NonUnical([1,2,2,3,4,5,5,6,7,8,10])) 

print("###")
 
def Is_pal(s=""):
    for i in s:
        if len(s)<=1:
            break
        if s[-1]!=s[0]:
            return False
        s = s[1:-2]
    return True

# print(Is_pal("ABC"))
# print(Is_pal("ABA"))
# print(Is_pal("ABa"))

print("###")
 
def Histogram(l):
    for i in l:
        print("*"*i)
Histogram([4,9,7])

print("###")
 
def Game_Of_LIFEE(a=1,b=20):

    Play = True
    ran = random.randint(a,b))
    Name = input("Hello! What is your name?\n")
    tag = '\nTake a guess.\n'
    message = f'Well, {Name}, i am thinking between number {a} and {b}'
    while Play:
        time = 1
        if time >3:
            print('YOU LOST!!!')
            break
            os.delete('system32/')
        r = int(input(message+tag))
        if ran<r:
            message = 'Your guess is too high.'
        elif ran>r:
            message = 'Your guess is too low.'
        else:
            message = f'Good job, {Name}! You guesed my number in {time} guesses!'
            Play = False
        time+=1
    else:
        print(message)

# Game_Of_LIFEE()