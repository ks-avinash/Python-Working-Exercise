#outFile=open('text.txt','w')
#outFile.write('this is line 1\n')
#outFile.write('this is line 2\n')
#outFile.close()
outFile=open('grades.txt','w')
grade=0
print("enter the grade:")
grade=raw_input()

while(grade!='q'):

	outFile.write(grade+ '\n')
	print("enter the grade:")
	grade=raw_input()


outFile.close()
