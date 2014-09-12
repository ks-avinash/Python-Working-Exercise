#N=range(1,101)
#EN=[X for X in N if X%2==0]
#print(EN)
sent="now is the time for all good people to come to the aid"
words=sent.split(' ')
wlen=[(word,len(word))for word in words]
for i in wlen:
    print(i)
print(words)