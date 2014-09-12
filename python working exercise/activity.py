msg="The recommended activity is: "
print("enter the temp")
temp=int(raw_input())
if temp>85:
	msg=msg+"swimming"
elif temp>=70:
	msg=msg+"tennis."
elif temp>=32:
       	msg=msg+"golf."
elif temp>=0:
       	msg=msg+"dancing."
else:
	msg=msg+"sitting by the fire"
print(msg)

