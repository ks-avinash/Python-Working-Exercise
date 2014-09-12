def square(number):
    return number*number
num=2
sqnum=square(num) #sqnum=square(2)
sqnumber=square    #sqnumber=square 
sqnum=sqnumber(2)  #sqnum=
print(sqnum)

numbers=[1,2,3,4,5]
numsqrs=list(map(square,numbers))
print(numsqrs)