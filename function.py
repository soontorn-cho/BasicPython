def hello(name):
    print(f"Hello {name}")


# สร้างฟังก์ชั่นแบบมีการ Return Value
def area(width, height):
    total = width * height
    return total


# เรียกใช้งานฟังก์ชั่น hello()
hello("Soontorn")
print(f"Area = {area(15,7.5)}")
print()

# ฟังก์ชันแบบมีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name : {name}")
    print(f"Name : {salary}")
    print(f"Name : {lang}")


show_info()
print()
show_info("Soontorn", 15000, 'Python')