import numpy as np

# a. Tạo ma trận khả nghịch 3x3
A = np.array([[2, 1, 3],
              [1, 1, 1],
              [3, 2, 4]])

# Kiểm tra khả nghịch bằng định thức
det_A = np.linalg.det(A)
print("Định thức của A:", det_A)

if det_A == 0:
    print("Ma trận KHÔNG khả nghịch.")
else:
    print("Ma trận khả nghịch. Nghịch đảo của A là:")
    print(np.linalg.inv(A))

# b. Nhập họ tên hoặc MSSV
text = input("Nhập họ và tên hoặc MSSV: ")

# c. Mã hóa chuỗi
# Chuyển các ký tự thành mã ASCII
ascii_codes = [ord(c) for c in text]

# Bổ sung số 0 để chia đều thành các khối 3 phần tử
while len(ascii_codes) % 3 != 0:
    ascii_codes.append(0)

# Chia thành các vector 3x1
vectors = [np.array(ascii_codes[i:i+3]) for i in range(0, len(ascii_codes), 3)]

# Mã hóa: Y = A * X
encoded_vectors = [A.dot(v) for v in vectors]

print("\nChuỗi sau khi mã hóa:")
for vec in encoded_vectors:
    print(vec)

# d. Giải mã: X = A⁻¹ * Y
A_inv = np.linalg.inv(A)
decoded_vectors = [np.round(A_inv.dot(vec)).astype(int) for vec in encoded_vectors]

# Nối lại thành chuỗi ký tự
decoded_ascii = [num for vec in decoded_vectors for num in vec if num != 0]
decoded_text = ''.join([chr(num) for num in decoded_ascii if 0 <= num < 256])

print("\nChuỗi sau khi giải mã:")
print(decoded_text)
