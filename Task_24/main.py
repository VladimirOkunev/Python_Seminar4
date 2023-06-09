# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего 
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым 
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.


import random


num = 12 #количество кустов на грядке

plant = [random.randint(0,20) for _ in range(num)]

print(plant)

sum = plant[-1] + plant[0] + plant[1]

for i in range(num-1):
    if sum < (plant[i-1] + plant[i] + plant[i+1]):
        sum = plant[i-1] + plant[i] + plant[i+1]
print(sum)