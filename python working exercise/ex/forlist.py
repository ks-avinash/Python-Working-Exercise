#print("sum is:" +str(sum))
words=("now","is","time","the")
for word in words:
    print word
    
    max=0
for i in range(1,len(words)):
    if len(words[i])>len(words[max]):
        max=i
print("the longest word is: " +words[max])