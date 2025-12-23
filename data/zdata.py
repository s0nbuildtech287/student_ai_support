import csv
import random

# Danh sách tên Việt
last_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Bùi", "Đặng", "Đỗ", "Vũ"]
middle_names = ["Văn", "Thị", "Minh", "Đức", "Xuân", "Quang", "Hồng"]
first_names = [
    "Sơn", "Huy", "Linh", "Anh", "Trang",
    "Phương", "Tuấn", "Nam", "Long", "Hà",
    "Khánh", "Duy", "Hiếu", "Thảo"
]

# Ngành + lớp
majors = {
    "HTTT": 4,
    "TTNT": 4,
    "CNPM": 4,
    "ATTT": 4
}

students = []

start_code = 2100
total_students = 100

for i in range(total_students):
    student_id = f"225116{start_code + i}"

    # Random tên
    name = f"{random.choice(last_names)} {random.choice(middle_names)} {random.choice(first_names)}"

    # Random lớp
    major = random.choice(list(majors.keys()))
    class_no = random.randint(1, majors[major])
    student_class = f"64{major}{class_no}"

    students.append([student_id, name, student_class])

# Ghi ra CSV
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["student_id", "name", "class"])
    writer.writerows(students)

print("✅ Đã tạo file students.csv với", total_students, "sinh viên")
