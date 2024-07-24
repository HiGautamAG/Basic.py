Start = 11
end = 95

print("Prime numbers between", Start, "and", end, "are:")

for num in range(Start, end + 1):
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)