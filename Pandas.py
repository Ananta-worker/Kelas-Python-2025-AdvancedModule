"""
Pandas
1. structure data: Dataframe (DataFrame = struktur class)
    data dari dictionary di convert ke struktur dataframe
2. Mengakses Nilai Dataframe
3. Menggali Informasi danri Dataframe
4. Menambahkan dan Menghapus Kolom/Baris pada Dataframe
5. Membuat Dataframe dari External Data
6. Membuat Plot/Grafik
"""
import pandas as pd
import random

# dictionary terdiri dari key dan value
data_nilai = {
    "Nama": ["Ansar", "Bombom", "Caca", "Didu", "Eeb", "Fitri"],
    "Jenis Kelamin": ["Laki-laki", "Laki-laki", "Perempuan", "Laki-laki", "Laki-laki", "Perempuan"],
    "Matematika": [random.randint(60, 100) for _ in range(6)],
    "Bahasa":  [random.randint(60, 100) for _ in range(6)],
    "Olah Raga":  [random.randint(60, 100) for _ in range(6)]
}

df = pd.DataFrame(data_nilai)
print(df)

# mengakses data Dataframe berdasarkan kolom
print(df["Nama"])

# mengakses data Dataframe berdasarkan baris(index)
print(df.loc[2])

# mengakses data Dataframe berdasarkan baris(index)
print(df["Jenis Kelamin"])

print(df["Jenis Kelamin"] == "Laki-laki")

filter_jenis_kelamin = df["Jenis Kelamin"] == "Laki-laki"
print(df[filter_jenis_kelamin])

filter_matematika = df["Matematika"] > 80
print(df[filter_matematika])

# Menggali informasi dari DataFrame
print(df["Matematika"].mean()) # tdk di bulatkan
# atau
print(round(df["Matematika"].mean(), 2))  # Menggunakan round()
# atau
print(f"{df['Matematika'].mean():.3f}")   # Menggunakan format string

print(round(df["Matematika"].median(), 2))
print(round(df["Matematika"].sum(), 2))     # nilai total

print(df["Olah Raga"].max())
print(df["Olah Raga"].min())

print(df.describe())    # yang memiliki nilai seperti bil integer
print(df.describe(include="object")) # mengambil tipe lain
print(df.sort_values(by="Nama"))    # mengurutkan tabel berdasarkan value "nama" (abjad)
print(df.sort_values(by="Matematika"))    # mengurutkan tabel berdasarkan value "Matematika" (nilai)
print(df.sort_values(by="Matematika", ascending=False)) # mengurutkan nilai dari besar ke kecil
print(df.value_counts("Jenis Kelamin"))  # menghitung jumlah item
