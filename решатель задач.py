def f1():
 chisla='0123456789'
 chisla_spisok=list(chisla)
 print(chisla_spisok)
 haming='0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
 haming_spisok=haming.split()
 print(haming_spisok)
 def distance(x,y):
     k=7
     for i in range(7):
         if x%10==y%10:
             k=k-1
         x=x//10
         y=y//10
     return k
 cod=int(input("код= "))
 min=distance(cod,int(haming_spisok[0]))
 imin=0
 for i in range(1,9):
     D=distance(cod,int(haming_spisok[i]))
     if D<min:
         min=D
         imin=i
 print(min)     
 if min==0:
     print(f"код верный: символ {chisla_spisok[imin]}")
 elif min==1:
     print(f"код исправлен: символ {chisla_spisok[imin]}")
 else:
     print("код неверный")

 def f2():
    a = "abwgdevijklmnoprstufhcqx"
    abc = list(a)
    print(abc)
    b = ".- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- -. --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-"
    abcm=b.split()
    print(abcm)
    abcm=b.split()
    text=input("Введите текст на английском: ")
    indm=""
    for i in range (len(text)):
        ind = abc.index(text[i])
        indm=indm + abcm[ind]
        print(f"{indm}")

def f3():
    print ("p=")
    a=int (input ())
    print ("Np=")
    b=int (input())
    c=1
    d=0
    while b>0:
        d=d+(b%10)*c
        c=c*a
        b=a//10
        print("N10=",d)
    p = int(input("vvedite p (2<p<=10):"))
    x,y = int(1),int(1)

def f4():
    for x in range (1,p):
     a=[]
    for y in range (1,p):
      z = (x*y//p)*10 + (x*y)% p
      a.append(z)
      print(a)
      
      def f5():
          for a in range (2):
              for b in range (2):
                  for c in range (2):
                      if (((a and not(b)<=c)==a)==0):
                          print(a,b,c)
x=input( '''выберите функцию:
1
2
3
4
5''' )
if x=='1':
    f1()
elif x=='2':
    f2()
elif x=='3':
    f3()
elif x=='4':
    f4()
elif x=='5':
    f5()
else:
    print ('неверно')

