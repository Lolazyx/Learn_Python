#ชนิดข้อมูล และตัวแปร (Data Type & Variable)
#โครงสร้างตัวแปร(Variable) : ชื่อตัวแปร = ค่าที่เก็บในตัวแปร

w = "ex3_datatype-variable" #string
x = 20 #integer
y = 2.99 #float
z = True #boolean

print(w)
print(x)
print(y)
print(z)

print("example" + str(x)) #string ไม่สามารถบวกกับ integer ได้ จึงต้องแปลง integer ให้เป็น string โดยใช้ str()
#str(integer หรือ ตัวแปรแปรที่เป็น integer)

#ตรวจชนิดของข้อมูลโดยใช้ type(ข้อมูล หรือ ตัวแปร)

#ตรวจชนิดข้อมูลของข้อมูล
print(type("lolazy"))
print(type(20))
print(type(1.06))
print(type(False))

#ตรวจชนิดข้อมูลของตัวแปร
print(type(w))
print(type(x))
print(type(y))
print(type(z))