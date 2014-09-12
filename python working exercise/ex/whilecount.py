#sum=0
#num=1
#while num<=10:
 #   sum=sum+num
    #num=num+1
#print("The sum is:" +str(sum))
bal=5000
rate=1.02
year=1
while year<=10:
    bal=bal*rate
    print("year:"+str(year) +": " + str(bal))
    year=year+1