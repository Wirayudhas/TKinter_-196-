import tkinter as tk  # Mengimpor library tkinter dan memberi alias 'tk' untuk membuat GUI.

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")  # Mengubah teks di label hasil_label menjadi "Prediksi Prodi: Teknologi Informasi"

# Membuat jendela utama
root = tk.Tk()  # Membuat jendela utama aplikasi Tkinter dan menyimpannya di variabel root
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela utama menjadi "Aplikasi Prediksi Prodi Pilihan"

# Menentukan ukuran dan posisi jendela
root.geometry("350x400")  # Mengatur ukuran jendela utama menjadi 350 piksel lebar dan 400 piksel tinggi

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))  # Membuat label judul dengan teks "Aplikasi Prediksi Prodi Pilihan" dan font Arial 16 bold
judul_label.pack(pady=0)  # Menempatkan label di jendela utama dengan padding vertikal sebesar 0 piksel

# Membuat 10 input nilai mata pelajaran
input_labels = []  # List kosong untuk menyimpan referensi label setiap mata pelajaran
input_entries = []  # List kosong untuk menyimpan referensi input (Entry) setiap mata pelajaran

for i in range(10):  # Loop untuk membuat 10 input nilai mata pelajaran
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")  # Membuat label untuk setiap mata pelajaran, dengan nomor sesuai indeks
    label.pack()  # Menempatkan label di jendela utama
    input_labels.append(label)  # Menambahkan label ke dalam list input_labels

    entry = tk.Entry(root)  # Membuat kolom input (Entry) untuk memasukkan nilai mata pelajaran
    entry.pack(pady=1)  # Menempatkan kolom input di jendela utama dengan padding vertikal 1 piksel
    input_entries.append(entry)  # Menambahkan kolom input ke dalam list input_entries

# Tombol untuk memprediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  # Membuat tombol dengan teks "Hasil Prediksi" dan menghubungkannya ke fungsi hasil_prediksi
prediksi_button.pack(pady=20)  # Menempatkan tombol di jendela utama dengan padding vertikal 20 piksel

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="Prediksi Prodi akan muncul di sini.", font=("Arial", 12))  # Membuat label hasil dengan teks default "Prediksi Prodi akan muncul di sini." dan font Arial 12
hasil_label.pack(pady=10)  # Menempatkan label hasil di jendela utama dengan padding vertikal 10 piksel

# Menjalankan GUI
root.mainloop()  # Memulai loop utama Tkinter yang membuat jendela tetap tampil sampai ditutup
