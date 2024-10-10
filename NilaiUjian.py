def nilai_ujian():  # Mendefinisikan fungsi bernama nilai_ujian
    while True:  # Memulai loop tak terbatas untuk terus meminta input
        # Meminta input dari user
        nilai = input("Masukkan nilai ujian anda: ")  # Mengambil input nilai ujian dari pengguna
        
        try:
            # Mengonversi input menjadi integer
            nilai = int(nilai)  # Mengonversi input yang diberikan oleh pengguna menjadi tipe integer
            
            # Memeriksa rentang nilai dan memberikan feedback
            if 90 <= nilai <= 100:  # Jika nilai antara 90 dan 100
                print("Feedback: sangat baik")  # Menampilkan feedback 'sangat baik'
            elif 80 <= nilai <= 89:  # Jika nilai antara 80 dan 89
                print("Feedback: baik")  # Menampilkan feedback 'baik'
            elif 70 <= nilai <= 79:  # Jika nilai antara 70 dan 79
                print("Feedback: cukup")  # Menampilkan feedback 'cukup'
            elif 60 <= nilai <= 69:  # Jika nilai antara 60 dan 69
                print("Feedback: kurang")  # Menampilkan feedback 'kurang'
            else:  # Jika nilai kurang dari 60
                print("Feedback: sangat kurang")  # Menampilkan feedback 'sangat kurang'

        except ValueError:  # Menangani kesalahan jika input bukan angka
            print("Input tidak valid, silahkan masukkan angka!")  # Memberikan pesan kesalahan input tidak valid

        # Menanyakan kepada pengguna apakah ingin melakukan pengecekan lagi
        pilihan = input("apakah ada yang ingin dicek lagi? (y/n): ") 
        if pilihan == 'n':  # Jika pengguna memilih 'n', maka program akan dihentikan
            print("program dihentikan")  
            break  # Keluar dari loop dan menghentikan program

# Memanggil fungsi untuk menjalankan program
nilai_ujian()  # Menjalankan fungsi nilai_ujian
