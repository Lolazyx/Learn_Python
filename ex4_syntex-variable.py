# เงื่อนไขการตั้งชื่อของตัวแปร

"""
1. สามารถตั้งเป็น ตัวอักษร ตัวเลข สัญลักษณ์ และต้องตรงกับเงื่อนไขข้อที่ 2
2. ตัวแปรไม่สามารถขึ้นต้นด้วย ตัวเลขและสัญลักษณ์ ยกเว้น Underscore ( _ )
3. ตัวแปรไม่สามารถตั้งตาม keyword
4. ตัวอักษรพิมพ์ใหญ่หรือพิมพ์เล็กจะต่างกัน
"""

name = "lolazy"
_1 = 10
_name = "Lolazy"
Name = 20
NaMe = 2.00

print(name)
print(_1)
print(_name)
print(NaMe)