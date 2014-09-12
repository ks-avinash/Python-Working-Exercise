print("enter a numeric grade:")
grade=int(raw_input())
if grade>=90:
	rank="A"
elif grade>=80:
	rank="B"
elif grade>=70:
	rank="C"
elif grade>=60:
	rank="D"
else:
	print("did not recognize input")
print("your grade is: " + rank)
