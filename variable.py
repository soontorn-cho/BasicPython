a = 3
b = 4.92
c = "itgenius"

print(a)
print(b)
print(c)
print(a, b, c)

# การสร้างตัวแปรหลายตัวในบรรทัดเดียวกัน
x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)

# Boolean
status = True
msg = False

print(status, msg)


# ตัวแปรแสดงผลร่วมกับข้อความ
# วิธีที่ 1  concat string
print("ราคาขายต่อชิ้น", b, "บาท มีจำนวน", a, "ชิ้น")

# วิธีที่ 2 string interpolation
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3 format string
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")

