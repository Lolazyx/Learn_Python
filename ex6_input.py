# function input

#input จะรับค่า string
fname = input("Name : ") #รับค่าจากคีย์บอร์ดมาเก็บไว้ในตัวแปร fname
lname = input("Last Name : ")
print("Your name :" + fname + " " + lname)

#แปลงค่าใน input ให้เป็น integer หรือ float ได้
#ex1 (แนะนำ)
num1 = int(input("Number1 : "))
num2 = int(input("Number2 : "))
results = num1 + num2
print("results : " + str(results))