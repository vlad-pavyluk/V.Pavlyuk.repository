

import math


class Students():
	def __init__(self,name,mark1,mark2,mark3,mark4,mark5,mark6,mark7,project):
		self.name = name
		self.mark1 = mark1
		self.mark2 = mark2
		self.mark3 = mark3
		self.mark4 = mark4
		self.mark5 = mark5
		self.mark6 = mark6
		self.mark7 = mark7
		self.project = project	

student_1 = Students("Костюк Микола","5","5","5","0","0","?","?","?")
student_2 = Students("Крупка Павло","5","4","5","0","0","?","?","?")
student_3 = Students("Максименко Владислав","5","5","5","0","10","?","?","?")
student_4 = Students("Мельник Владислав","5","5","5","0","10","?","?","?")
student_5 = Students("Німченко","0","0","0","0","0","?","?","?")
student_6 = Students("Павлюк Владислав","5","5","5","5","10","?","?","?")
student_7 = Students("Рибак Ярослав","0","4","5","0","0","?","?","?")
student_8 = Students("Романенко Данііл","5","5","5","0","0","?","?","?")
student_9 = Students("Сиропятов Ігор","5","5","0","5","10","?","?","?")
student_10 = Students("Сокрут Данило","5","5","5","5","10","?","?","?")
student_11 = Students("Степаненко Михайло","5","5","5","5","10","?","?","?")
student_12 = Students("Томулець Максим","5","5","5","5","10","?","?","?")
student_13 = Students("Форбз Марія","5","5","5","5","10","?","?","?")
student_14 = Students("Хорольський Олексій","5","5","5","5","10","?","?","?")
student_15 = Students("Цегельник Денис","5","5","5","5","0","?","?","?")

print('У нас є журнал оцінок наших студентів за виконання лабораторних робіт')
a = input('Вам цікаво дізнатися?\n')
if a != "Ні":
	print('Спочатку ми вам покажемо оцінки всіх студентів')
	mar_1 = print(student_1.name + ' - ' + student_1.mark1 + ' - ' + student_1.mark2 + ' - ' + student_1.mark3 + ' - ' + student_1.mark4 + ' - ' + student_1.mark5 + ' - ' + student_1.mark6 + ' - ' + student_1.mark7)
	mar_2 = print(student_2.name + ' - ' + student_2.mark1 + ' - ' + student_2.mark2 + ' - ' + student_2.mark3 + ' - ' + student_2.mark4 + ' - ' + student_2.mark5 + ' - ' + student_2.mark6 + ' - ' + student_2.mark7)
	mar_3 = print(student_3.name + ' - ' + student_3.mark1 + ' - ' + student_3.mark2 + ' - ' + student_3.mark3 + ' - ' + student_3.mark4 + ' - ' + student_3.mark5 + ' - ' + student_3.mark6 + ' - ' + student_3.mark7)
	mar_4 = print(student_4.name + ' - ' + student_4.mark1 + ' - ' + student_4.mark2 + ' - ' + student_4.mark3 + ' - ' + student_4.mark4 + ' - ' + student_4.mark5 + ' - ' + student_4.mark6 + ' - ' + student_4.mark7)
	mar_5 = print(student_5.name + ' - ' + student_5.mark1 + ' - ' + student_5.mark2 + ' - ' + student_5.mark3 + ' - ' + student_5.mark4 + ' - ' + student_5.mark5 + ' - ' + student_5.mark6 + ' - ' + student_5.mark7)
	mar_6 = print(student_6.name + ' - ' + student_6.mark1 + ' - ' + student_6.mark2 + ' - ' + student_6.mark3 + ' - ' + student_6.mark4 + ' - ' + student_6.mark5 + ' - ' + student_6.mark6 + ' - ' + student_6.mark7)
	mar_7 = print(student_7.name + ' - ' + student_7.mark1 + ' - ' + student_7.mark2 + ' - ' + student_7.mark3 + ' - ' + student_7.mark4 + ' - ' + student_7.mark5 + ' - ' + student_7.mark6 + ' - ' + student_7.mark7)
	mar_8 = print(student_8.name + ' - ' + student_8.mark1 + ' - ' + student_8.mark2 + ' - ' + student_8.mark3 + ' - ' + student_8.mark4 + ' - ' + student_8.mark5 + ' - ' + student_8.mark6 + ' - ' + student_8.mark7)
	mar_9 = print(student_9.name + ' - ' + student_9.mark1 + ' - ' + student_9.mark2 + ' - ' + student_9.mark3 + ' - ' + student_9.mark4 + ' - ' + student_9.mark5 + ' - ' + student_9.mark6 + ' - ' + student_9.mark7)
	mar_10 = print(student_10.name + ' - ' + student_10.mark1 + ' - ' + student_10.mark2 + ' - ' + student_10.mark3 + ' - ' + student_10.mark4 + ' - ' + student_10.mark5 + ' - ' + student_10.mark6 + ' - ' + student_10.mark7)
	mar_11 = print(student_11.name + ' - ' + student_11.mark1 + ' - ' + student_11.mark2 + ' - ' + student_11.mark3 + ' - ' + student_11.mark4 + ' - ' + student_11.mark5 + ' - ' + student_11.mark6 + ' - ' + student_11.mark7)
	mar_12 = print(student_12.name + ' - ' + student_12.mark1 + ' - ' + student_12.mark2 + ' - ' + student_12.mark3 + ' - ' + student_12.mark4 + ' - ' + student_12.mark5 + ' - ' + student_12.mark6 + ' - ' + student_12.mark7)
	mar_13 = print(student_13.name + ' - ' + student_13.mark1 + ' - ' + student_13.mark2 + ' - ' + student_13.mark3 + ' - ' + student_13.mark4 + ' - ' + student_13.mark5 + ' - ' + student_13.mark6 + ' - ' + student_13.mark7)
	mar_14 = print(student_14.name + ' - ' + student_14.mark1 + ' - ' + student_14.mark2 + ' - ' + student_14.mark3 + ' - ' + student_14.mark4 + ' - ' + student_14.mark5 + ' - ' + student_14.mark6 + ' - ' + student_14.mark7)
	mar_15 = print(student_15.name + ' - ' + student_15.mark1 + ' - ' + student_15.mark2 + ' - ' + student_15.mark3 + ' - ' + student_15.mark4 + ' - ' + student_15.mark5 + ' - ' + student_15.mark6 + ' - ' + student_15.mark7)
else:
	print("Ну тоді допобачення!")

print('Як ви бачите,то в оцінках присутні "?",це значіть,що роботу ще не здали,або заняття з цією роботою ще не було')

while True:
	b = input('Про кого ви хочете дізнатися більше?\n')
	if b == "Костюк Микола":
		print('Зараз повторимо вам його оцінкі')
		print (student_1.name + ' - ' + student_1.mark1 + ' - ' + student_1.mark2 + ' - ' + student_1.mark3 + ' - ' + student_1.mark4 + ' - ' + student_1.mark5 + ' - ' + student_1.mark6 + ' - ' + student_1.mark7)	
	elif b == "Крупка Павло":
		print('Зараз повторимо вам його оцінкі')
		print(student_2.name + ' - ' + student_2.mark1 + ' - ' + student_2.mark2 + ' - ' + student_2.mark3 + ' - ' + student_2.mark4 + ' - ' + student_2.mark5 + ' - ' + student_2.mark6 + ' - ' + student_2.mark7)
	elif b == "Максименко Владислав":
		print('Зараз повторимо вам його оцінкі')
		print(student_3.name + ' - ' + student_3.mark1 + ' - ' + student_3.mark2 + ' - ' + student_3.mark3 + ' - ' + student_3.mark4 + ' - ' + student_3.mark5 + ' - ' + student_3.mark6 + ' - ' + student_3.mark7)
	elif b == "Мельник Владислав":
		print('Зараз повторимо вам його оцінкі')
		print(student_4.name + ' - ' + student_4.mark1 + ' - ' + student_4.mark2 + ' - ' + student_4.mark3 + ' - ' + student_4.mark4 + ' - ' + student_4.mark5 + ' - ' + student_4.mark6 + ' - ' + student_4.mark7)
	elif b == "Німченко":
		print('Зараз повторимо вам його оцінкі')
		print(student_5.name + ' - ' + student_5.mark1 + ' - ' + student_5.mark2 + ' - ' + student_5.mark3 + ' - ' + student_5.mark4 + ' - ' + student_5.mark5 + ' - ' + student_5.mark6 + ' - ' + student_5.mark7)
	elif b == "Павлюк Владислав":
		print('Зараз повторимо вам його оцінкі')
		print(student_6.name + ' - ' + student_6.mark1 + ' - ' + student_6.mark2 + ' - ' + student_6.mark3 + ' - ' + student_6.mark4 + ' - ' + student_6.mark5 + ' - ' + student_6.mark6 + ' - ' + student_6.mark7)
	elif b == "Рибак Ярослав":
		print('Зараз повторимо вам його оцінкі')
		print(student_7.name + ' - ' + student_7.mark1 + ' - ' + student_7.mark2 + ' - ' + student_7.mark3 + ' - ' + student_7.mark4 + ' - ' + student_7.mark5 + ' - ' + student_7.mark6 + ' - ' + student_7.mark7)
	elif b == "Романенко Данііл":
		print('Зараз повторимо вам його оцінкі')
		print(student_8.name + ' - ' + student_8.mark1 + ' - ' + student_8.mark2 + ' - ' + student_8.mark3 + ' - ' + student_8.mark4 + ' - ' + student_8.mark5 + ' - ' + student_8.mark6 + ' - ' + student_8.mark7)
	elif b == "Сиропятов Ігор":
		print('Зараз повторимо вам його оцінкі')
		print(student_9.name + ' - ' + student_9.mark1 + ' - ' + student_9.mark2 + ' - ' + student_9.mark3 + ' - ' + student_9.mark4 + ' - ' + student_9.mark5 + ' - ' + student_9.mark6 + ' - ' + student_9.mark7)
	elif b == "Сокрут Данило":
		print('Зараз повторимо вам його оцінкі')
		print(student_10.name + ' - ' + student_10.mark1 + ' - ' + student_10.mark2 + ' - ' + student_10.mark3 + ' - ' + student_10.mark4 + ' - ' + student_10.mark5 + ' - ' + student_10.mark6 + ' - ' + student_10.mark7)
	elif b == "Степаненко Михайло":
		print('Зараз повторимо вам його оцінкі')
		print(student_11.name + ' - ' + student_11.mark1 + ' - ' + student_11.mark2 + ' - ' + student_11.mark3 + ' - ' + student_11.mark4 + ' - ' + student_11.mark5 + ' - ' + student_11.mark6 + ' - ' + student_11.mark7)
	elif b == "Томулець Максим":
		print('Зараз повторимо вам його оцінкі')
		print(student_12.name + ' - ' + student_12.mark1 + ' - ' + student_12.mark2 + ' - ' + student_12.mark3 + ' - ' + student_12.mark4 + ' - ' + student_12.mark5 + ' - ' + student_12.mark6 + ' - ' + student_12.mark7)
	elif b == "Форбз Марія":
		print('Зараз повторимо вам його оцінкі')
		print(student_13.name + ' - ' + student_13.mark1 + ' - ' + student_13.mark2 + ' - ' + student_13.mark3 + ' - ' + student_13.mark4 + ' - ' + student_13.mark5 + ' - ' + student_13.mark6 + ' - ' + student_13.mark7)
	elif b == "Хорольський Олексій":
		print('Зараз повторимо вам його оцінкі')
		print(student_14.name + ' - ' + student_14.mark1 + ' - ' + student_14.mark2 + ' - ' + student_14.mark3 + ' - ' + student_14.mark4 + ' - ' + student_14.mark5 + ' - ' + student_14.mark6 + ' - ' + student_14.mark7)
	elif b == "Цегельник Денис":
		print('Зараз повторимо вам його оцінкі')
		print(student_15.name + ' - ' + student_15.mark1 + ' - ' + student_15.mark2 + ' - ' + student_15.mark3 + ' - ' + student_15.mark4 + ' - ' + student_15.mark5 + ' - ' + student_15.mark6 + ' - ' + student_15.mark7)	
	else:
		print("Ну тоді добре")
		break	

print("Потрібно зазначити,що максимальна кількість балів для кожного студента за індивідуальний проект дорівнює 20")
print('Також максимальна кількість балів за здачу однієї лабораторної роботи на 20')
print('Кількість лабораторних робіт в курсі дорівнює 7 для кожного студента')
print('Також ми не можемо визначити,частку балів від максимуму,для отримання автомата,адже ми не знаємо,скільки балів потрібно отримати для автомата')
print('Вибачте,але на цьому функціонал нашої програми закінчується,дякую за увагу!')