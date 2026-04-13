p=int(input("Enter a number.."))
b=int(input("Enter a number.."))
r=int(input("Enter a choice.."))
def interest(p,b,r):
   if(r==1):
     s=(p*b*12)/100
   elif(r==2):
     s=(p*b*10)/100
   else:
     print("Invalid value..")
     return None
   return s  
si=interest(p,b,r)
print("Simple interest for the respective customer is..",si)
