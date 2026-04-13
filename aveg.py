t=int(input("Enter the Tamil mark.."))
e=int(input("Enter the English mark.."))
m=int(input("Enter the Maths mark.."))
p=int(input("Enter the Physics mark.."))
c=int(input("Enter the Chemistry mark.."))
def operation(t,e,m,p,c):
   s=t+e+m+p+c
   print("The total mark of the student is..",s)
   avg=s/5
   print("The average of the student is..",avg)
operation(t,e,m,p,c)
