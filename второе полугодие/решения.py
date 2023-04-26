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
#12.1      
sp=[]
for num in range(117,1000):
    if all(num%delit!=0 for delit in range(2, num-1)):
        sp.append(num)
print(sp) 

#14
a='0123456789abcd'
for x in a:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(f//14)
        break 
        
        
#23
from itertools import product
for i in range (2,6):
  b=product('12',repeat=5)
  for n in b:
    a= 12
    for x in n:
      if x=='1':
        a-=1
      else:
        a*=7
    if a==489:
      print(n)
        
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            #numb=''.join(n)
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2

            if a==y: count+=1
    return count
                
print(f23(1,10,10)*f23(10,35,25))
        
#16.1
import sys
sys.setrecursionlimit(3050)
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print (f(2023)/f(2020))

#16.2

itog1=itog2=1
for x1 in range(1,2024):
    itog1=itog1*x1
for x2 in range(1,2021):
    itog2=itog2*x2
print(itog1/itog2)

#17

with open('17.txt') as f:
    a=[int(x) for x in f]
    abs=list(map(abs,a))
for i in range(len(a)-1):
    if(a[i]%10==3 and a[i+1]%10!=3) or (a[i]%10!=3 and a[i+11]==3):
                                        count=+1
 print(count)
sp=[]

#24.1
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*':
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)

#24.2
s=open('24.txt').readline().replace('AB','1').replace('AC','1')
s=s.replace('A', '').replace('B',' ').replace('C',' ')
print(max(len(x) for x in s.split()))

#25.1
for i in range (2023,10**10,2023):
    n=str(i)
    if n[0]=='1' and n[2:6]=='2139' and n[-1]=='4': print(i,i/2023)
    
#25.2
for a in range(10):
        for b in range(10):
            x=int(f'12345{a}6{b}8')
            if x%17==0:
                print(x,x//17)

  #26
  
  with open('26.txt') as f:
    m=[int(x) for x in f]
    m.pop(0)
    m.sort(reverse=True)
    k,mini=1,m[0]
    for i in range(1,len(m)):
        if m[i]+3<=mini:
            mini=m[i]
            k+=1
print(k,mini)


#27
with open ('27_A.txt') as f:
    n=[x for x in f]
    n.pop(0)
    sp=[]
    k=[]
    ind=[]
    for i in n:
        sp.append(list(map(int,i.split())))
    for i in range(len(sp)):
        k.append((sp[i][1]-1)//36+1)
    for i in range(len(sp)):
        ind.append(sp[i][0])
    sp=list(zip(ind,k))
    costs=[]
    for i in sp:
        pos=i[0]
        cost=0
        for x in sp:
            cost=cost+abs(pos-x[0])*x[1]
        costs.append(cost)
    print(min(costs))
with open ('27_B.txt') as f: #открываем файл
    n=[x for x in f] #записываем строки
    n.pop(0) #убираме первую строку
    sp=[]
    k=[]
    ind=[]
    for i in n:
        sp.append(list(map(int,i.split()))) #переводим значения в списке в числа
    for i in range(len(sp)):
        k.append((sp[i][1]-1)//36+1) #находим кол-во контейнеров
    for i in range(len(sp)):
        ind.append(sp[i][0] #сохраняем километраж пунктов 
    sp=list(zip(ind,k)) #соединяем километраж и кол-во контейнеров
    costs=[]
    for i in range(549715,549735,1):#в этом цикле выводим значения приближаясь к минимальному
        pos=sp[i][0]
        cost=0
        for x in sp:
            cost=cost+abs(pos-x[0])*x[1] #вычисляем стоимость
        costs.append(cost)
        print(i,sp[i][0],cost)
#Ответ 5634689219329
#олимпиадная какая-то
from itertools import product		
lox=[0,712,673,1075,875,1622,423]		
ggh=[712,0,1385,1800,1577,2348,1128]		
opd=[673,1385,0,1499,239,2046,244]		
mer=[1075,1800,1499,0,1287,551,1266]		
tin=[875,1577,239,1287,0,1835,442]		
pav=[1622,2348,2046,551,1835,0,1813]		
kaa=[423,1128,244,1266,442,1813,0]
tabl=[lox,ggh,opd,mer,tin,pav,kaa]		
alf='0123456'		
a=product(alf,repeat=7)		
maxi=0		
for i in a:
    if all(i.count(x)==1 for x in alf):
        s=0
        for l in range(len(i)-1):
            s+=tabl[int(i[l])][int(i[l+1])]
            if s >=maxi:
                maxi=s
                
print(maxi)	
