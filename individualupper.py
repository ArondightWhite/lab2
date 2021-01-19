print("Individual Upper var1\n"
      "Write digits numbers")

a1 = int(input("First digit of number 1: "))
a2 = int(input("Second digit of number 1: "))
b1 = int(input("Single digit: "))

SumRes = a1+a2+b1
FD = int((a1+a2+b1) % 10)
SD = int((a1+a2+b1) / 10)

print("First digit of new number = {0}\nSecond digit of number = {1}".format(FD, SD))