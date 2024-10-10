def tekanan_darah():  # Mendefinisikan fungsi tekanan_darah
    while True:  # Memulai loop tak terbatas untuk terus meminta input
        # Meminta input usia dan tekanan darah dari user
        usia = input("Masukkan Usia Anda: ")  # Meminta pengguna memasukkan usia
        tekanan_darah = input("Masukkan Tekanan Darah Anda: ")  # Meminta pengguna memasukkan tekanan darah

        try:
            # Mengonversi input usia dan tekanan darah menjadi integer
            usia = int(usia)  # Mengonversi input usia menjadi integer
            tekanan_darah = int(tekanan_darah)  # Mengonversi input tekanan darah menjadi integer
            
            # Mengecek status kesehatan berdasarkan usia dan tekanan darah
            if usia >= 60 and tekanan_darah > 140:  # Jika usia >= 60 dan tekanan darah > 140
                print("Status Kesehatan: Tekanan Darah Tinggi")  # Menampilkan status tekanan darah tinggi
            elif usia >= 60 and tekanan_darah <= 140:  # Jika usia >= 60 dan tekanan darah <= 140
                print("Status Kesehatan: Normal")  # Menampilkan status normal
            elif usia < 60 and tekanan_darah > 130:  # Jika usia < 60 dan tekanan darah > 130
                print("Status Kesehatan: Tekanan Darah Tinggi")  # Menampilkan status tekanan darah tinggi
            else:  # Jika kondisi di atas tidak terpenuhi
                print("Status Kesehatan: Normal")  # Menampilkan status normal

        except ValueError:  # Menangani kesalahan jika input bukan angka
            print("Input tidak valid, silahkan masukkan angka!")  # Menampilkan pesan kesalahan

        # Meminta pengguna untuk melanjutkan atau tidak
        pilihan = input("apakah ada yang ingin dicek lagi? (y/n)")  # Menanyakan kepada pengguna untuk melanjutkan
        if pilihan == 'n':   # Jika pengguna memilih 'n', maka program akan dihentikan'
            print("program dihentikan") 
            break  # Keluar dari loop dan menghentikan program

# Memanggil fungsi untuk menjalankan program
tekanan_darah()
