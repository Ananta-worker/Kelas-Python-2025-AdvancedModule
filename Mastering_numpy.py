"""
menjalankan numpy
"""

import numpy as np

a = [1, 2, 3]
arr_a = np.array(a)
print(arr_a)
b = [[1, 2, 3], [4, 5, 6]]
arr_b = np.array(b)
print(arr_b)
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_c = np.array(c)
print(arr_c)
print("Array setelah reshape:")
reshape_arrc = arr_c.reshape(1, 9)      # (baris, kolom)
print(reshape_arrc)
np.append(arr_c, 10)    # belum merubah, dipanggil array kembali ke awal
print(arr_c)
arr_c = np.append(arr_c, 10)    # array berubah
print(arr_c)

# indexing, slicing
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr_c = np.array(c)
print("array asal")
print(arr_c)
print("mengambil baris ke-2, kolom ke-3")
print(arr_c[1, 2])
print(arr_c[1, 0:3])    # mengambil baris ke-2(index 1), kolom ke,1-3(index 0,1,2)

# operation pada array
print("operation pada array")
print(arr_c)
print(arr_c+10)
print(arr_c>3)

print("filter ------")
filter_arr = arr_c <= 3
print(filter_arr)
filtered_arr_c = arr_c[filter_arr]
print(filtered_arr_c)
