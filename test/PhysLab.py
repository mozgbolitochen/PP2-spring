def avg(list):
    sum,it = 0,0
    for i in list:
        sum+=i
        it+=1
    return sum/it
for i in range(5):
    list = map(float,input().split())
    print(avg(list))

