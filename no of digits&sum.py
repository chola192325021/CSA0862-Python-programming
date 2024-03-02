n=eval(input("enter the number:"))
s=0
while(n!=0):
    s+=n%10
    n//=10
print("sum of digits:",s)
