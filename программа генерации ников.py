#подключение библиотеки random
import random
#переозбразование строки в символьный массив
def stringappendarray(mystring, myarray):
	for i in mystring:
		myarray.append(i)
#сортировка символьных массивов
def myarraysort(myarray):
	for i in range(0, len(myarray), 1):
		for j in range(0, len(myarray), 1):
			if (myarray[i] < myarray[j]):
				temp=myarray[i]
				myarray[i]=myarray[j]
				myarray[j]=temp
#генерация никнеймов
def mygenerate(myarray):
	n=int(input("введите количество символов в никнейме -- "))
	r=int(input("введите количество генерованых никнеймов -- "))
	k=0
	temp="\nрезультаты генерации:\n\n"
	while (k < r):
		for i in range(0, n, 1):
			temp=temp+myarray[random.randint(0, len(myarray)-1)+0]
		temp=temp+"\n"
		k=k+1
	print(temp, "\n")
#проверка ввода и запуск задачи программы
def myactivity():
	startreplay="1"
	while (startreplay == "1"):
		errorreplay="1"
		while (errorreplay == "1"):
			myanswer=input("генерация с буквамы = 1; генерация с буквамы и цифрамы = 2; ваш выбор -- ")
			if (myanswer == "1" or myanswer == "2"):
				errorreplay="0"
			else:
				print("выберите с команд!")
		if (myanswer == "1"):
			mygenerate(myarrayletters)
		else:
			mygenerate(myarraylettersnumbers)
		startreplay=input("запуск программы еще раз = 1; ваш выбор -- ")	
#главная программа
print("---начало программы---")
myletters="zxcvbnmqwertyuiopasdfghjkl"
mylettersnumbers="zxcvbnmqwertyuiopasdfghjkl1234567890"
myarrayletters=[]
myarraylettersnumbers=[]
stringappendarray(myletters, myarrayletters)
stringappendarray(mylettersnumbers, myarraylettersnumbers)
myarraysort(myarrayletters)
myarraysort(myarraylettersnumbers)
myactivity()
temp=input("---для полного завершения программы, нажмите любую клавишу---\n")