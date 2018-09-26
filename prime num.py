print("find the number 0f prime number between 2 intervels")
    a=int(input("i="))
    b=int(input("r="))
        if(a,b<=100000)
          flag=0
          c=0
         for x in range(a,b+1):
          flag=0
         for y i range(1,x+1):
          if(x%y==0):
            flag=flag+1
           if(flag==2):
              c=c+1
            print c
          else:
              print("invalid")
