print("TO CHECK WHEATHER A NUMBER IS ARMSTRONG OR NOT")
   n=int(input("N="))
   t=n
   s=0
   a=0
 while n>0:
    re=n%10
    a=re**3
    s=s+a
    n=n//10
  if(t==s):
    print("armsrong")
   else:
    print("not armsrong")
