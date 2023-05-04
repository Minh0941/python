import time
import random
def gend_rand(n):
    start = time.time()
    listing=[]
    for i in range(n):
        listing.append(random.randint(0,n))

    end= time.time()
    print(f"Elapsed time: {end-start} seconds")

gend_rand(100000)


def sum_rand(n):
    j=0
    start= time.time()
    for i in range(n):
        j+=i
    end=time.time()
    print(F"Time Elapsed: {end-start} seconds")
 
sum_rand(1000000)

def sumlist_pretend_slice_1(vals):
    start=time.time()
    sum=0
    while len(vals)>0:
        sum+=vals[0]
        vals=vals[1:]
    end=time.time()
    print(F"{end-start} seconds")
    return sum
def main():
    listing=[]
    for items in range(100000):
        listing.append(items)
    return listing
x= main()
sumlist_pretend_slice_1(x)