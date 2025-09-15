
import time
import random

startingTime = time.time()

list1 = random.sample(range(1,1000001),1000000)
list1.sort()

print(list1)

duration = time.time()-startingTime
print(duration)