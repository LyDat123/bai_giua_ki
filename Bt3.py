class Student:

    def __init__(self, name, ap_mark, security_mark, web_mark):
        self.name = name
        self.ap_mark = round(ap_mark, 1)
        self.security_mark = round(security_mark, 1)
        self.web_mark = round(web_mark, 1)

    def __str__(self):
        return f'{self.name}, {self.ap_mark}, {float(self.security_mark)}, {self.web_mark}'

    def averageMark(self):
        avg = (self.ap_mark + self.security_mark + self.web_mark) / 3
        return avg

    def highestMark(self):
        highestMark = max(self.ap_mark, self.security_mark, self.web_mark)
        return highestMark

    def highestAvgMark(self):
        return self.averageMark()


def findHighestAvgMark(arr):
    highestAvg = 0
    highestStudent = None
    for student in arr:
        avg = student.averageMark()
        if avg > highestAvg:
            highestAvg = avg
            highestStudent = student
    return highestStudent


def main():
    fisrtStudent = Student('Dat', 1.21, 8, 10)
    print(fisrtStudent)
    print(f"Diem trung binh 3 mon: {round(fisrtStudent.averageMark(), 1)}")
    print(f"Diem lon nhat cua 3 mon: {fisrtStudent.highestMark()}")
    print()
    soLuongSinhVien = int(input("Nhập số lượng sinh viên cần thêm: "))
    arr = []
    for i in range(soLuongSinhVien):
        print(f"Sinh viên thứ {i + 1}")
        name = input("Tên: ")
        ap_mark = float(input("Điểm LTNC: "))
        security_mark = float(input("Điểm Bảo Mật: "))
        web_mark = float(input("Điểm Web: "))
        if 0 <= ap_mark <= 10 or 0 <= security_mark <= 10 or 0 <= web_mark <= 10:
            student = Student(name, ap_mark, security_mark, web_mark)
            avg_Mark = student.averageMark()
            print(f"Diem trung binh 3 mon: {avg_Mark}")
            print(student)
            arr.append(student)
        else:
            print("Số nhập không hợp lệ!")

    highestStudent = findHighestAvgMark(arr)
    print(f"Sinh viên có điểm trung bình 3 môn cao nhất: {highestStudent}")

if __name__ == '__main__':
    main()
