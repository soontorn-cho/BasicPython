scores = {
    'james': 1828,
    'thomas': 3628,
    'danny': 9310
}
scores['bobby'] = 4401
numbers = {1: 'One', 2: 'Two', 3: 'Three'}
print(scores)
print(numbers)

print(scores['bobby'])

# เพิ่มสมาชิกใหม่ลง dictionary
scores['Soontorn'] = 4500
print(scores)

# การสร้าง dictionary ว่าง
points = {}
# เพิ่มค่าเข้า dictionary ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

# การ loop อ่านสมาชิกทั้งหมดของ Dictionary ออกมา
for k, v in scores.items():
    print(k,v)


