"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

lengthA = input(int())
lengthB = input(int())
a = list(range(int(lengthA)))
b = list(range(int(lengthB)))
print('введите числа 1 списка')
for i in a:
    a[i] = input()
print('введите числа 2 списка')
for i in b:
    b[i] = input()

c = []

a = sorted(set(a))
b = sorted(set(b))

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)