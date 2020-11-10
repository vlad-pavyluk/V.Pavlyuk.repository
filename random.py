first = ('break','choose','forge','freeze','get','speak','steal','tear','wake')
second = ('bet','burst','cast','cut','fit','hit','hurt','let','put','quit','rid''set')
thirsd = ('bring','buy','catch','flight','seek','teach','think','keep','sleep','feel','bleed')


import random
count = 0

print('Ви можете скласти випадкову фразу на основі трьох списків')

while True:
    a = input('Будете брати слово?\n')
    if a == "Так":
        first += second and thirsd 
        fi = (random.choice(first))
        print(fi)
        count += 1
        print('У вас уже %d слово(а)'%count)
    elif count == 1:
        print('Вашим другим словом буде')
        second += first and thirsd 
        sec = (random.choice(second))
        print(sec)
        count += 1
        break
    else: 
        print ('Вашим останнім словом буде')
        thirsd  += second and first 
        th = (random.choice(thirsd))
        print(th)
        count += 1
        break
print('Ви вже маєте %d слів'%count)
a = input("Чи хочете ви їх об'єднати?\n")
if a == "Так":
    my_list = []
    my_list.append(th)
    my_list.append(fi)
    print('Дякую за увагу!')
else:
   print("Тоді допобачення!")
 
  


    