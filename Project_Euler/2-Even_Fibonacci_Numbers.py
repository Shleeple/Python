num1 = 1
num2 = 2
total_sum = 2
while num2 < 4000000:
    num1, num2 = num2, num2+num1
    if num2 % 2 == 0:
        total_sum += num2
print(total_sum)