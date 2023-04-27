import time
from bing_image_downloader import downloader
import os
import random

x = input('masukkan gambar yang ingin dicari : ')
print("Contoh : \nD:\\dataset_untuk_machine_learning\\penelusuran_bing")
direktori = input("Path ke direktori :")
while True:
	try:
		downloader.download(x, limit=10,adult_filter_off=True, output_dir=direktori,force_replace=False)
		break
	except Exception as e:
		print(f'{e} gagal mendownload gambar... mengulang dalam 1 Menit')
		time.sleep(60)
# direktori dataset
direktori_new = (f'{direktori}\\{x}')
# List semua file dalam folder
gambar = os.listdir(direktori_new)

# Ambil 5 gambar secara acak
pilihan = random.sample(gambar, 5)

# Loop untuk mengambil gambar
for gambar in pilihan:
    # Lakukan sesuatu dengan gambar
    print(f"Gambar yang diambil: {gambar}")
