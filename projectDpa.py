# Program To-Do List Sederhana
# Dibuat oleh: 1. Ricky Darmawan : 2517052015
             # 2.Chelsea Alifah Islamy Munawar : 2517052011


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




