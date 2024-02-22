import datetime as d
hay = d.date.today()
hay = hay.__add__(d.timedelta(-5))
#print(hay)

print('###')

# print('Yesterday:',d.date.today().__add__(d.timedelta(-1)))
# print('Today:',d.date.today())
# print('Today:',d.date.today().__add__(d.timedelta(1)))

print('###')

a = d.datetime.today()
print(a.microsecond)

print('###')

b = d.datetime.today()
# print(b.)