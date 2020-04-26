number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jany', 'Wasan']
mixed = [10, 25, 75, True, 'Soontorn']

# การเข้าถึงสมาชิกใน list

print(number[1])
print(name[3])
print(mixed[2], mixed[4])
print(number)

# การนับจำนวนสมาชิกใน list
print("สมาชิกทั้งหมดของ  number = ", len(number))

# การสร้าง list แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกเข้าไปใน list ว่าง
data.append(10)
data.append(15)
data.append(20)

print(data)

# การอัพเดทสมาชิกใน list

data[1] = 12

print(data)

# ฟังก์ชั่นวน loop อ่านสมาชิกทั้งหมด
num = 0
sum = 0

for n in number:
    print(n)


for num in number:
    sum += num

    print(sum)
