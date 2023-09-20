sum = 0
cnt = 0
while True:
    number = (input("Enter a number: "))
    if number == "done":
        break
    try:
        number = int(number)
        sum += number
        cnt += 1
    except ValueError:
        print("invalid input. enter a number")
if cnt > 0:
    average = sum / cnt
else:
    average = 0
print("Sum of input numbers : ", sum)
print("number of input : ", cnt)
print("Average of input numbers : ", average)
