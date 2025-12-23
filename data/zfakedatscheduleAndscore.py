import csv
import random

# ---------- LOAD STUDENTS ----------
students = []
with open("students.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append(row)

# ---------- LOAD SUBJECTS ----------
subjects_by_major = {}
subjects = []

with open("subjects.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        subjects.append(row)
        subjects_by_major.setdefault(row["major"], []).append(row)

# ---------- TIME & ROOM ----------
days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6"]
times = ["07:30-09:30", "09:30-11:30", "13:00-15:00"]
rooms = ["A101", "A203", "B202", "C301"]

schedule_rows = []
score_rows = []

for student in students:
    student_id = student["student_id"]
    student_class = student["class"]

    # Lấy ngành từ class (64HTTT4 → HTTT)
    major = student_class[2:6]

    # Mỗi SV học 3–5 môn
    available_subjects = subjects_by_major[major]
    enrolled_subjects = random.sample(
        available_subjects,
        random.randint(3, min(5, len(available_subjects)))
    )

    for subj in enrolled_subjects:
        # ---------- SCHEDULE ----------
        schedule_rows.append({
            "student_id": student_id,
            "subject_id": subj["subject_id"],
            "day": random.choice(days),
            "room": random.choice(rooms),
            "time": random.choice(times)
        })

        # ---------- SCORES ----------
        mid = round(random.uniform(6.0, 9.0), 1)
        final = round(random.uniform(6.0, 9.5), 1)
        total = round((mid + final) / 2, 1)

        score_rows.append({
            "student_id": student_id,
            "subject_id": subj["subject_id"],
            "mid": mid,
            "final": final,
            "total": total
        })

# ---------- WRITE schedule.csv ----------
with open("schedule.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["student_id", "subject_id", "day", "room", "time"]
    )
    writer.writeheader()
    writer.writerows(schedule_rows)

# ---------- WRITE scores.csv ----------
with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["student_id", "subject_id", "mid", "final", "total"]
    )
    writer.writeheader()
    writer.writerows(score_rows)

print("✅ Đã tạo schedule.csv & scores.csv thành công")