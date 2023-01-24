def f5():
  for N in range(516):
  b = f'{N:b}'
  if N % 2 == 0:
    b +='10'
else:
  b = '1' + b + '01'
if int(b,2) > 516:
  print(N)
  'break'

 #8 
count=0 
for a in range (1,8): 
    for b in range (8): 
        for c in range (8): 
            for d in range (8): 
                for e in range (8): 
                    s=str(a)+str(b)+str(c)+str(d)+str(e) 
                    if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0: 
                        count+=1 
                    if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0: 
                        count+=1 
                    if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0: 
                        count+=1 
print(count) 

#8(2) 
from itertools import product 
nums=product('01234567',repeat=5) 
k=0 
n='16 36 56 76 61 63 65 67' 
nn=n.split() 
for n in nums: 
    numb=''.join(n) 
    sp=[] 
    if numb.count('6')==1 and numb[0]!='0': 
        for x in nn: 
            if x in numb: 
                sp.append(x) 
        if not sp:  
            k+=1 
print(k)

#6(черепаха)

from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(5)
done()

#12
sp=[]
for i in range(2,1000):
  n=0
  for k in range (2,117+4*i-1):
      if (117+4*i)%k==0:
          n=1
          break
  if n==0:
      print(i)
      print(117+4*i)
      break
 

#14
a='0123456789abcd'
for x in a:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(f//14)
        break 
