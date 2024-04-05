def findMinValue(D):
    minValue = float('inf')
    for i in D:
        if D[i] < minValue:
            minValue = D[i]
    return minValue


def sumValue(D):
    sum = 0
    for i in D:
        sum += D[i]
    return sum


def main():
    L = [
        "doublemint,1.5,10",
        "mentos,0.7,20",
        "oreo,2.8,5",
        "chupachups,0.2,30"
    ]
    # Tao Dict moi
    D = {}
    print("Danh sách sản phẩm:")
    for chuoi in L:
        phanTu = chuoi.split(',')
        ten = phanTu[0]
        giatien = float(phanTu[1])
        soluong = int(phanTu[2])
        D[ten] = soluong
    print(D)
    # Tìm value bé nhất
    minValue = findMinValue(D)
    print(f"Giá trị nhỏ nhất là: {minValue}")
    # Tính tổng value
    sum = sumValue(D)
    print(f"Tổng các value là: {sum}")


if __name__ == '__main__':
    main()
