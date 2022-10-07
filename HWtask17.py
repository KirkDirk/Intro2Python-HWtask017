# Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.

somenum = int(input('Введите натуральное число N: '))
somelist = []
for i in range(2, somenum+1):
    while somenum % i == 0 and i <= somenum: 
        somelist.append(i)
        somenum /= i
print(somelist)