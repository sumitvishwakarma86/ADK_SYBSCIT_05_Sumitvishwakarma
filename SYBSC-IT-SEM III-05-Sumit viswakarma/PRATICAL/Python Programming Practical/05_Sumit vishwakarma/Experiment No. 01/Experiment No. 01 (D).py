num = int(input("enter number for reverse: "))
r=0
while num !=0:
    b=num%10
    r=r*10+b
    num//=10
print("reverse number: ",r)
