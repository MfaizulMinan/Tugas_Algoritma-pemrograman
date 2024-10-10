def cek_ganjil_genap():
    while True:  # Memulai loop tak terbatas untuk terus meminta input
        # Meminta input dari user
        nilai = input("Masukkan sebuah angka: ")
        
        try:
            # Mengonversi input menjadi integer
            nilai = int(nilai)

            # Mengecek apakah bilangan tersebut ganjil atau genap
            if nilai % 2 == 0:  # Jika nilai habis dibagi 2, maka bilangan genap
                print(f"Angka {nilai} adalah bilangan genap.")
            else:  # Jika tidak, maka bilangan ganjil
                print(f"Angka {nilai} adalah bilangan ganjil.")
        
        except ValueError:  # Menangani kesalahan jika input bukan angka
            print("Input tidak valid. Silakan masukkan angka!")
            continue  # Kembali ke awal loop untuk meminta input lagi
        
        # Penawaran untuk melanjutkan atau mengakhiri program
        pilihan = input("Ada yang ingin dicek lagi? (y/n): ").lower()  
        if pilihan == 'n':  # Jika pengguna memilih 'n', maka program akan dihentikan
            print("Program dihentikan.")  
            break  # Keluar dari loop dan menghentikan program
        
# Memanggil fungsi untuk menjalankan program
cek_ganjil_genap()