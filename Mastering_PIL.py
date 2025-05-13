# PIL Python Imaging Library

from PIL import Image
import matplotlib.pyplot as plt

# membuka gambar
canva = Image.open("canva_01.jpg")

# menampilkan gambar
plt.imshow(canva)
# plt.axis('off')  # Menyembunyikan sumbu
plt.show()

# Mengubah gambar menjadi greyscale
greyscale_image = canva.convert('L')

# Menampilkan gambar greyscale
plt.imshow(greyscale_image, cmap='gray')
plt.axis('off')
plt.show()

print(canva.size)

# Definisikan area crop (left, upper, right, lower)
crop_area = (150, 180, 900, 420)

# Crop gambar
cropped_image = canva.crop(crop_area)

# Menampilkan gambar hasil crop
plt.imshow(cropped_image)
plt.axis('off')
plt.show()


