print("-----------------------------------------------")
print("# Summation Program")
print("# Type 'exit' to end the program")
print("-----------------------------------------------")

# ตัวแปรไว้เก็บผลรวม

sumdata = 0
count = 1

while True:
    data = input(f"Enter number {count} : ")
    #ตรวจสอบว่าผู้ใช้ป้อน 'exit'
    if(data == "exit"):
        break
    #การหาผลรวม
    sumdata += int(data)
    count = count + 1

print(f"Sum value is {sumdata}")
