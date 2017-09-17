def Factorial(num):
    new_num=1
    for count in range(num,1,-1):
        new_num *=count
    return new_num
def s():
  limit1=int(input('enter num'))
  limit2=int(input('enter num'))
  for n in range (limit1,limit2+1):
      print(n,'!=' ,Factorial(n),sep='')
s()


