import os
files=os.popen('dir *.py')
filesit=iter(files)
#print(next(filesit))
#print(next(filesit))
#print(next(filesit))
#print(next(filesit))
#print(next(filesit))
#print(next(filesit))
#print(next(filesit))
for file in files:
	print(file)
