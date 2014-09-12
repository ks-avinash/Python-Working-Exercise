def hypo(s1,s2):
    def square(num):
        return num*num
    return math.sqrt(square(s1)+square(s2))
print("Enter the length of side1:")
side1=int(raw_input())
print("Enter the length of side2:")
side=int(raw_input())
hyp=hypo(side1,side2)
print(str(hyp))