class gen1:
    def __init__(self,stop=10,start=0):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.stop:
            raise StopIteration
        x = self.start
        self.start +=1
        return x*x

    
# mynums = gen1()
# for i in mynums:
#     print(i)

#########################
    
class gen2:
    def __init__(self,stop= 11):
        self.start = 0
        self.end = stop/2
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        z = self.start
        self.start += 1
        return 2*z

# ns = gen2(int(input()))
# somestr = ""
# for i in ns:
#     somestr+=str(i)
#     somestr+=', '
# print(somestr[0:-2])
    
#########################

def gen3(start=0,stop=12):
    while start<=stop:
        if not start%3 or not start%4:
            yield start
        start+=1

# sl = list(gen3(0,12))
# print(sl)

#########################

def squares(start=0,stop=12):
    while start<=stop:
        yield start**2
        start+=1

# sq = squares()
# sqit = iter(sq)
# for i in sqit:
#     print(i)

#########################

def gen5(start=12,end=0):
    while start>=end:
        yield start
        start-=1

# g5 = gen5()
# for i in g5:
#     print(i)
        