n= int(input("enter the number of terms needed= "))
p=0
f=int(input("enter the first term= "))
s=int(input("enter the second term= "))
for i in range (0,n):
    p=f+s
    print(p, end=" ")    
    f=s
    s=p 
