a = int(input("enter the number "))
first = a // 1000
second = a // 100
second_1 = second % 10
third = a // 10
third_1 = third % 100
third_2 = third_1 % 10
th4 = a % 10
print(first - th4 + second_1 - third_2)