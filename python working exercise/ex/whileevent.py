avg=0.0
total=0
count=0
print ("Enter a grade:")
grade=int(raw_input())
while grade!=-1:
    total=total +grade
    count=count+1
    print("enter a grade")
    grae=int(raw_input())
avg=total/count
print("avg grade: "+str(avg))