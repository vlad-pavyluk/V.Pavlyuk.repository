options = [1,2,3,4,5,6]

import random
random.shuffle(options)

print('Нам потрібно знайти правильні варіанти контрольної,всього є шість варіантів')
count = int(0)
q = input('Ви можете нам допомогти? y/n\n')
if q == 'y':
        print('Давайте почнемо')
        
elif q == 'n':
        print('Ну добре,допобачення')
while True:
    w = input('Будеш доставати варіант? y/n\n')  
    if w == 'y':
       current = options.pop()
       print('Тобі випав варіант %d' %current)
       count += int(current)
       if int('3')<count>int('3'):
           print('Це не той варіант')
           break
       elif count == int('3'):
           print('Це те,що нам потрібно')
           break
       else:
            print('У тебе уже %d варіант' %count)
    elif w == 'n':
         print('У тебе уже %d варіант'%count)
         break
        
        
print('Дякую за допомогу,до зустрічі')
    
