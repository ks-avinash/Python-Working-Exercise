numer=0
denom=0
while denom !=-1:
    print("enter a numerator:")
    numer=float(raw_input())
    print ("enter the denom")
    denom=float(raw_input())
    if denom==0:
        continue
        print(numer/denom)