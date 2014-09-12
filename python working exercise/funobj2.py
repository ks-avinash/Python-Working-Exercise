def sum(x,y):
    return x+y
import functools
num=list(range(1,11))
sum=functools.reduce(sum,num)
print(sum)