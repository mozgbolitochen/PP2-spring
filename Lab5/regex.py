import re
#word = input()
word = 'I am, the worst human being, EVER created. Hating myself is the main reason i am alive'
#1
pattern = re.compile(r'ab*')
# print(pattern.findall(word))

##################################################
#2
pattern = re.compile(r'abbb?')
# print(pattern.findall(word))
pattern = re.compile(r'ab{2,3}') 
# print(pattern.findall(word))

##################################################
#3

pattern = re.compile(r'([a-z]_)+[a-z]')
# print(pattern.findall(word))
pattern = re.compile(r'[a-z]+_')
# print(pattern.findall(word))

##################################################
#4

pattern = re.compile(r'[A-Z][a-z]+')
# print(re.findall(word))

##################################################
#5

pattern = re.compile(r'a.*b')
# print(pattern.findall(word))

##################################################
#6

pattern = re.compile(r'[ ,.]')
# print(pattern.sub(':',word))

##################################################
#7

word = 'i_am_the_best and_you_are_the_worst mu_ha_ha_ha_ha_ha_ha_ha' 
def repl(s):
    res = ''
    group = s.group(1)
    res = group.capitalize()
    group = s.group(2)
    for stri in group[1:].split('_'):
        res+= stri[0].capitalize()+stri[1:]
    return res
pattern = re.compile(r'([A-Za-z]+)((_[A-Za-z]+)+)')
# print(pattern.sub(repl,word))
def reaplace(s):
    if s.group(1):
        return s.group(1).capitalize()
    elif s.group(2):
        return ' '+s.group(2)[1:].capitalize()
    else:
        return s.group(3)[1:].capitalize()        
pattern = re.compile(r'(^[A-Za-z])|( [A-Za-z])|(_[A-Za-z])')
# print(pattern.sub(reaplace,word))
##################################################
#8
#Write a Python program to split a string at uppercase letters.
word = 'WordsAreWorldRulers' #('Words' 'Are' 'World' 'Rulers')
pattern = re.compile(r'[A-Z]')
print(pattern.split(word))

##################################################
#9
def repla(s):
    return ' '+s.group()
pattern = re.compile(r'[A-Z]')
# print(pattern.sub(repla,word))


##################################################
#10
#Write a Python program to convert a given camel case string to snake case.

word = 'Write a Python program to convert a given camel case string WordsAreWorldRulers' 

def replac(s):
    if s.group(1):
        return s.group(1).lower()
    else:
        return '_'+s.group(2).lower()

pattern = re.compile(r'(^[A-Z])|( [A-Z])|([A-Z])')
print(pattern.sub(replac,word))