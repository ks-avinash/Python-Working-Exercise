def ftoc(temp):
    return (temp-32.0) * (5.0/9.0)


def ctof(temp):
    return temp *(9.0/5.0) + 32.0

def convert(temp,toScale):
    if toScale.lower()=="c":
        return ftoc(temp)
    else:
        return ctof(temp)
print("enter a temp: ")
temp=int(raw_input())
print("enter the scale to temp")
scale=raw_input()
convtemp=convert(temp,scale)
print temp,convtemp,scale
