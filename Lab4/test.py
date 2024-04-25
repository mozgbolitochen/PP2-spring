import time
def m(n):
    return n*11
i = [1,2,3,4,5,6,7,8,9]
i = list(map(m,i))
# print(i)

####################################################################################################

def fil_u(s=''): 
    if not s.islower():
        return True
    else:
        return False
def fil_l(s=''): 
    if s.islower():
        return True
    else:
        return False
# s = input().split()
# count_of_lower = len(list(filter(fil_l,s)))
# count_of_upper = len(list(filter(fil_u,s)))    
# print(count_of_lower, count_of_upper)

####################################################################################################

def ispal(s):
    return s==''.join(reversed(s))
# print(ispal(input()))

####################################################################################################

# problem = int(input('what is your problem?)?)?)0\n'))
# milesecs = int(input('do you want to sleeep?)?)?)0\n'))
# time.sleep(milesecs*(10**-3))
# print('here is root of your problem after you slept',milesecs, 'mileseconds',problem**0.5)

####################################################################################################

tuple = (0,1,2,3)
# print(all(tuple))                                                                                 X   t