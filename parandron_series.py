n=int(input("enter the number= "))
rv=0
m=n
while n!=0:
   t=n%10
   rv=(10*rv)+t
   n=n//10
if rv==m:
   print("the string is parandron")
else:
   print("the string is not parandron")
