# Program To-Do List Sederhana
# Dibuat oleh: 1. Ricky Darmawan : 2517052015
             # 2. Chelsea Alifah Islamy Munawar : 2517052011
             # 3. putria alya maharani : 2517052014


# List untuk menyimpan semua task (collection)
todos = []

# Fungsi: Tampilkan Semua Task
def tampilkan_task():
    if len(todos) == 0:
        print("\nBelum ada task.\n")
    else:
        print("\n=== Daftar Task ===")
        for i, task in enumerate(todos):
            print(f"{i+1}. {task['judul']} - {task['deskripsi']}")
        print()


# Fungsi: Tambah Task
def tambah_task():
    print("\n=== Tambah Task ===")
    judul = input("Masukkan judul task : ")
    deskripsi = input("Masukkan deskripsi task : ")

    # Membuat dictionary untuk menyimpan 1 task
    task = {
        "judul": judul,
        "deskripsi": deskripsi
    }

    todos.append(task)
    print("Task berhasil ditambahkan!\n")


# Fungsi: Edit Task
def edit_task():
    tampilkan_task()

    if len(todos) == 0:
        return

    try:
        indeks = int(input("Pilih nomor task yang ingin diedit: ")) - 1
        
        if indeks < 0 or indeks >= len(todos):
            print("Nomor task tidak valid!\n")
            return

        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah)")
        judul_baru = input("Judul baru: ")
        deskripsi_baru = input("Deskripsi baru: ")

        if judul_baru != "":
            todos[indeks]["judul"] = judul_baru
        
        if deskripsi_baru != "":
            todos[indeks]["deskripsi"] = deskripsi_baru

        print("Task berhasil diperbarui!\n")

    except ValueError:
        print("Input harus berupa angka!\n")


# Fungsi: Cari / Filter Task
def cari_task():
    keyword = input("\nMasukkan kata kunci pencarian: ").lower()

    hasil = []
    for task in todos:
        if keyword in task["judul"].lower() or keyword in task["deskripsi"].lower():
            hasil.append(task)

    if len(hasil) == 0:
        print("Tidak ada task yang cocok.\n")
    else:
        print("\n=== Hasil Pencarian ===")
        for i, task in enumerate(hasil):
            print(f"{i+1}. {task['judul']} - {task['deskripsi']}")
        print()


# Fungsi: Hapus Task
def hapus_task():
    tampilkan_task()

    if len(todos) == 0:
        return
    try:
        indeks = int(input("Pilih nomor task yang ingin dihapus: ")) - 1

        if indeks < 0 or indeks >= len(todos):
            print("Nomor task tidak valid!\n")
            return

        del todos[indeks]
        print("Task berhasil dihapus!\n")

    except ValueError:
        print("Input harus berupa angka!\n")


# Menu Utama Program
def menu():
    while True:
        print("=== PROGRAM TO-DO LIST ===")
        print("1. Tambah Task")
        print("2. Tampilkan Task")
        print("3. Edit Task")
        print("4. Hapus Task")
        print("5. Cari / Filter Task")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_task()
        elif pilihan == "2":
            tampilkan_task()
        elif pilihan == "3":
            edit_task()
        elif pilihan == "4":
            hapus_task()
        elif pilihan == "5":
            cari_task()
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")



# Program Dimulai
menu()



