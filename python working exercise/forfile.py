#inFile=open('text.txt','r')
#line=inFile.readline()
#for line in open('text.txt'):
   #print (line,end='')
sum=0
count=0
for grade in open('grades.txt'):
	print(grade)
	sum=sum+int(grade)
	count=count+1
print ("Sum:="+str(sum)) 
