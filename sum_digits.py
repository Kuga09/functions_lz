def sum_digits(a):
    sum=0
    for i in range(0,len(a)):
        sum+=int(a[i])
    print('Сумма всех цифр числа',a,'=',sum)
print('Введите число:')
a=input()
sum_digits(a)