#การแปลงชนิดของข้อมูล Type Conversion
#using str() int() float()

x = "10" #string
y = 112 #integer
z = 3.14 #float

# string => integer
print(int(x) + y)
# or
results_1 = int(x)
print(results_1 + y)

# string => float
print(float(x) + z)
# or
results_2 = float(y)
print(results_2 + z)

#integer => string
print(str(y) + x)
#or
results_3 = str(z)
print(results_3 + x)