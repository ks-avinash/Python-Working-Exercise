print("enter hours-worked:")
work=int(raw_input())
rate=25.00
if work>40:
	grosspay=(40*rate) +((work-40)*(rate*1.5))
else:
	grosspay=work*rate
print("grosspay:" + str(grosspay))
