def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return str(fact)
print("enter the num")
no=int(raw_input())
print(fact(no))
