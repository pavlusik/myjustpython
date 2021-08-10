"""сумма первых n натуральных парных и непарных чисел графически"""
n=int(input("введте число n = "))
pic1=""
pic2=""
sum1=0
sum2=0
for i in range(1, 2*n+1, 1):
  if (i%2 == 0):
    if (i != 2*n):
      pic1=pic1+str(i)+"+"
      sum1=sum1+i
    else:
      sum1=sum1+i
      pic1=pic1+str(i)+"="+str(sum1)
  else:
    if (i != 2*n-1):
      pic2=pic2+str(i)+"+"
      sum2=sum2+i
    else:
      sum2=sum2+i
      pic2=pic2+str(i)+"="+str(sum2)
print("\n\n\nсумма первых n парных натуральных чисел:\n", pic1,"\n\n\nсумма первых n непарных натуральных чисел:\n", pic2)