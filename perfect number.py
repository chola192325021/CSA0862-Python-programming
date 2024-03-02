n=1000
r=0
for i in range(1,n):
  if(n%i==0):
      r=r+i
  if(r==n):
     print("its a perfect number",n)
     break
  else:
      print("its not a perfect number")
      break
