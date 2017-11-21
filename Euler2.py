import time
fibs = [1,2]
maxFib = 4*10**6
length = len(fibs)
start_time = time.time();
while(fibs[length-1]+fibs[length-2] < maxFib):
    fibs.append(fibs[length-1]+fibs[length-2])
    length = len(fibs)

theSum = sum(filter(lambda arg: arg % 2 == 0,fibs))
print(str(time.time()-start_time)+"\n")
print(theSum)
