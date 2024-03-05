n=input("enter the string:")
count=0
coun=0
s=0
a=len(n)
for b in n:
    if b in ('aeiouAEIOU'):
        count=count+1
    elif b in(' .,;'):
        s=s+1
    else:
        coun=coun+1
print("no of ovwels:",count)
print("no of consonants:",coun)
