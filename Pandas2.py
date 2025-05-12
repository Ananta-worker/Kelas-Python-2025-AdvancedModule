"""
Pandas 2
"""
import pandas as pd
import random
import matplotlib.pyplot as plt

data_nilai = {
    "Nama": ["Ansar", "Bombom", "Caca", "Didu", "Eeb", "Fitri"],
    "Jenis Kelamin": ["Laki-laki", "Laki-laki", "Perempuan", "Laki-laki", "Laki-laki", "Perempuan"],
    "Matematika": [random.randint(60, 100) for _ in range(6)],
    "Bahasa":  [random.randint(60, 100) for _ in range(6)],
    "Olah Raga":  [random.randint(60, 100) for _ in range(6)]
}

df_nilai = pd.DataFrame(data_nilai)
print(df_nilai)

keterampilan = {
    "Keterampilan": [random.randint(60, 100) for _ in range(6)]
}

df_keterampilan = pd.DataFrame(keterampilan)
print(df_keterampilan)

pd.concat([df_nilai, df_keterampilan], axis=1)  # Menggabungkan dua tabel
df_nilai = pd.concat([df_nilai, df_keterampilan], axis=1)
print(df_nilai)

df_nilai["Total"] = df_nilai["Matematika"] + df_nilai["Bahasa"] + df_nilai["Olah Raga"] + df_nilai["Keterampilan"]
print(df_nilai.sort_values(by="Total", ascending=False))    # mengurutkan kolom Total dari besar kekecil

# menambahkan baris pada table
murid_baru = {
    "Nama": ["Jessica"],
    "Jenis Kelamin": ["Perempuan"],
    "Matematika": 70,
    "Bahasa":  82,
    "Olah Raga": 87,
    "Keterampilan": 78,
    "Total": 317
}
print(pd.DataFrame(murid_baru, index=[6]))

df_nilai = pd.concat([df_nilai, pd.DataFrame(murid_baru, index=[6])])
print(df_nilai)     # menggabungkan tabel

df_nilai.drop("Keterampilan", axis=1, inplace=True)     # menghapus kolom
print(df_nilai)

df_nilai.drop(5, axis=0, inplace=True)      # menghapus baris
print(df_nilai)
# mengambil data dari table excel, install dulu openpyxl, pip install openpyxl / lewat seting
df_murid = pd.read_excel("daftar nilai.xlsx", index_col="No")
print(df_murid)

# Membuat grafik/plot dari tabel
# sebelumnya install dulu lewat terminal - pip install pandas matplotlib
# import matplotlib.pyplot as plt

df_murid.plot(x="Nama", y="Matematika", kind="barh")    # barh (bar arah horisontal) bar (bar arah vertikal)
plt.title("Nilai Matematika Siswa")
plt.xlabel("Nilai Matematika")
plt.ylabel("Nama siswa")
plt.show()

df_murid.plot(x="Nama", y=["Matematika", "Bahasa"], kind="barh")    # barh (bar arah horisontal) bar (bar arah vertikal)
plt.title("Nilai Matematika Siswa")
plt.xlabel("Nilai Matematika")
plt.ylabel("Nama siswa")
plt.show()