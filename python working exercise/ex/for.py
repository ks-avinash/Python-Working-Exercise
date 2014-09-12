#for i in [1,2,3,4,5]:
 #   print(i)
a=[1,2,3,4,5]
sum=0
for i in a:
    sum=sum+i
print(sum)
word="hello"
for letter in word:
    print(letter)
    
sentence="now is the time for all good people to come to the aid"
count=0
for let in sentence:
    if let=='a'or let=='e' or let=='i' or let=='o' or let=='u':
        count=count+1
print("the number of vowels is: " + str(count))
                                