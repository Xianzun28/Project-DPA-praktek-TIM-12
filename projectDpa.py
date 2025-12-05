# Program To-Do List Sederhana
# Dibuat oleh: 1. Ricky Darmawan : 2517052015


# List untuk menyimpan semua task (collection)
todos = []

def tampilkan_task():
    if len(todos) == 0:
        print("\nBelum ada task.\n")
    else:
        print("\n=== Daftar Task ===")
        for i, task in enumerate(todos):
            print(f"{i+1}. {task['judul']} - {task['deskripsi']}")
        print()


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
