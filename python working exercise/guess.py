answer="avinash"
print("here is a guess game.you get three tries.")
print("What is the name of the computer that played on Jeopardy?")
response=raw_input()
if response==answer:
	print("that is right!")
else:
	print("sorry.guess again:")
	response==raw_input()
	if response ==answer:
		print("that is right")
	else:
		print("sorry one more guess:")
		response==raw_input()
		if response==answer:
			print("that is right!")
		else:
			print("sorry.No more guesses.The answer is "+ answer+".")
