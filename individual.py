import math

print("Individual var1\n"
      "Write 2 numbers")

Num1 = int(input("1st num: "))
Num2 = int(input("2st num: "))

AverageResult = (abs(Num1)+abs(Num2))/2
GeometricMeanResult = math.sqrt(abs(Num1)+abs(Num2))

print("Arithmetical mean = %.2f\n"
      "GeometricMean = %.2f" % (AverageResult, GeometricMeanResult))

