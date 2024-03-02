n=eval(input("enetr the number:"))
s=0
for i in str(n):
    s+=n%10
    n//=10
print("sum of digits:",s)
