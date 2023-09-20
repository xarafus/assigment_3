hours = int(input("Enter hours : "))
rate = int(input("Enter rate: "))
if hours <= 40:
    salary = float(hours * rate)
else:
    xhours = hours - 40
    salary = (xhours * 1.5 * rate) + (40 * rate)
print("Pay : ", salary)
