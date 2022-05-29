s=input()
s=list(s)
i=-1
temp=0
while i<=len(s)-2:
    i=i+1
    if(i%2==1):
        temp=s[i-1]
        s[i-1]=s[i]
        s[i]=temp
print(*s,sep='')
