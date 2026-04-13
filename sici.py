a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
x=(-1*b)/(2*a)
y=(b*b)-(4*a*c)
if (y<0):
   k=((-y)**0.5)/(2*a)
   print("root1=",x,"+j",k)
   print("root2=",x,"-j",k)
elif (y>0):
   d=x+((y**0.5)/(2*a))
   e=x-((y**0.5)/(2*a))
   print("root1=",d)
   print("root2=",e)
else:
   print("root=",x)
