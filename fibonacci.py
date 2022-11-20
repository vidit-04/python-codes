k=int(input('k: '))
fibs=[0]
prev=0
cur=1
temp=0
i=0
sum1=0
print('0')
while(temp<k):
    print(cur)
    fibs.append(cur)
    temp=prev+cur
    prev=cur
    cur=temp
while(i<len(fibs)):
    if i%2==0:
        sum1+=fibs[i]
    i+=1
print('sum:',sum1)