a=int(input())
b=list()
c=0
for i in range(0,a,1);
    c=int(input())
    b.append(int(c))
#print(b)
 x=0
 y=0
 for i in range(0,a,1):
    x=x+b[i];
 for j in range(i+1,a,1);
    y=y+b[j]
  try:
      if((x//(i+1))==(y//(a-i-1)));
      print("yes")
          break
      except:
          print("no")
          y=0;
