
#Найдите сумму цифр трехзначного числa.
a = int(input("Введите трёхзначное число: "))
b = a % 10
a = a // 10
c = a % 10
a = a // 10

print("Сумма всех цифр числа:", a + b + c)