def square(num):
    return num*num

def numVowels(string):
    string=string.lower()
    count=0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] =="u":

           count+=1
    return count
#print("enter a num: ")
#num=int(input())
#numsquared=square(num)
#print(str(num) + " squared =" +str(numsquared))
print("enter a string: ")
strng = raw_input()
vowel=str(numVowels(strng))
print(vowel)
