from tabulate import tabulate
import datetime
import sys
import time 

time_now = datetime.datetime.now()
print()



PRODUK = [
    {"no": 1, "product_id": 1083, "produk": "susu", "stok": 10, "tanggal kadaluarsa": "2025-08-01", "tanggal masuk": "2025-01-02", "kategori penyimpanan": "suhu ruangan", "kategori makanan": "minuman"},
    {"no": 2, "product_id": 4721, "produk": "mie", "stok": 19, "tanggal kadaluarsa": "2025-11-19", "tanggal masuk": "2025-02-04", "kategori penyimpanan": "suhu ruangan", "kategori makanan": "makanan kering"},
    {"no": 3, "product_id": 9056, "produk": "keju", "stok": 2, "tanggal kadaluarsa": "2025-10-05", "tanggal masuk": "2024-12-06", "kategori penyimpanan": "suhu pendingin", "kategori makanan": "olahan susu"},
    {"no": 4, "product_id": 2345, "produk": "mentega", "stok": 17, "tanggal kadaluarsa": "2025-09-03", "tanggal masuk": "2024-05-08", "kategori penyimpanan": "suhu ruangan", "kategori makanan": "olahan susu"},
    {"no": 5, "product_id": 7890, "produk": "coklat", "stok": 3, "tanggal kadaluarsa": "2024-01-12", "tanggal masuk": "2023-05-10", "kategori penyimpanan": "suhu pendingin", "kategori makanan": "makanan manis"},
    {"no": 6, "product_id": 6472, "produk": "teh", "stok": 35, "tanggal kadaluarsa": "2025-08-25", "tanggal masuk": "2024-10-12", "kategori penyimpanan": "suhu ruangann", "kategori makanan": "minuman"},
    {"no": 7, "product_id": 3108, "produk": "air mineral", "stok": 31, "tanggal kadaluarsa": "2025-05-26", "tanggal masuk": "2024-09-14", "kategori penyimpanan": "suhu ruangan", "kategori makanan": "minuman"},
    {"no": 8, "product_id": 5913, "produk": "chiki", "stok": 20, "tanggal kadaluarsa": "2025-07-10", "tanggal masuk": "2024-11-16", "kategori penyimpanan": "suhu ruangan", "kategori makanan": "camilan"},
    {"no": 9, "product_id": 4420, "produk": "kentaki", "stok": 100, "tanggal kadaluarsa": "2025-12-01", "tanggal masuk": "2024-07-18", "kategori penyimpanan": "freezer", "kategori makanan": "makanan beku"},
    {"no": 10, "product_id": 2084, "produk": "roti", "stok": 8, "tanggal kadaluarsa": "2025-12-11", "tanggal masuk": "2024-02-20", "kategori penyimpanan": "suhu ruangan", "kategori makanan": "makanan siap saji"}
]

Tujuan_Barang = ["Gudang Alfamart", "Gudang Indomaret", "Tip Top", "Mall Bandung", "Gudang Indofood", "Gudang Bogor", "Gudang Jakarta"]


def animation(teks, delay = 0.05):
    for i in teks:
        print(i, end='', flush=True)
        time.sleep(delay)

    print()
def main_menu():
    print("-------------------------------------------")
    print("""
        SELAMAT DATANG DI DIVISI SALES \n
        MENU SELECTION:  
          1. Daftar Produk
          2. Cari Produk 
          3. Status Produk
          4. Produk Stok Rendah
          5. Hapus Produk
          6. EXIT
""")
    
def sub_menu():
     print("-------------------------------------------")
     print("""
    SUB MENU: PRODUCT LIST
          1. Tampilkan Daftar Produk  
          2. Tambah Barang Masuk
          3. Catat Barang keluar
          4. Kembali ke Main menu
""")
     
def show_product():
    count = len(PRODUK[0])
    print(tabulate(PRODUK, headers='keys', tablefmt='fancy_grid', colalign=("center",)*count))
    animation("Data Produk berhasil ditampilkan", 0.03)

def product_masuk():
    while True:
        print("-------------------------------------------")
        print("""
    SUB MENU: Barang Masuk
        1. Tambah Barang Masuk
        2. Kembali ke Menu sebelumnya 
""")
        try: 
            option = int(input("Input menu [1-2]: "))
        except ValueError:
            animation("Invalid Input: [1-2]", 0.03)
            continue
        
        if option == 1:
            while True:
                print()
                animation("Note: ID Product hanya 4 angka",0.03)
                input_id = input("Input ID Product: ")

                if len(input_id) != 4 or not input_id.isdigit():
                    animation("Invalid Input: ID Product tidak sesuai",0.03)
                    continue

                input_id = int(input_id)

             
                for data in PRODUK:
                    if input_id == data["product_id"]:
                        print(f"ID {input_id} sudah ada dengan produk '{data['produk']}'")
                        confirm = input("Ingin menambah stok? [Yes/No]: ").lower()
                        if confirm == "yes":
                            try:
                                add_stok = int(input("Tambah stok: "))
                                data["stok"] += add_stok
                                animation("Stok berhasil ditambah",0.03)
                            except ValueError:
                                animation("Invalid Input: Masukkan Angka",0.03)
                                count = len(PRODUK[0])
                                print(tabulate(PRODUK, headers='keys', tablefmt='fancy_grid', colalign=('center',) * count))
                        return  

               
                input_product = input("Input Product: ").lower()

                for data in PRODUK:
                    if data["produk"] == input_product:
                        print(f"Data '{input_product}' sudah ada dengan ID Product {data['product_id']}")
                        return  

                try:
                    add_stok = int(input("Input Stok: "))
                except ValueError:
                    print("Invalid Input: Masukkan Angka")
                    continue

                while True:
                    input_tanggal_Kadaluarsa= input("Input Tanggal Kadaluarsa [yyyy-mm-dd]: ")
                    try:
                        tanggal_input = datetime.datetime.strptime(input_tanggal_Kadaluarsa, "%Y-%m-%d").date()
                        today = datetime.datetime.today().date()
                        if tanggal_input <= today:
                            animation("Invalid: Produk sudah kadaluarsa",0.03)
                            continue
                        else:
                            break
                    except ValueError:
                        animation("Invalid Input: Format tanggal salah",0.03)

                while True:
                    input_tanggal_masuk = input("Input Tanggal Masuk [yyyy-mm-dd]: ")
                    try:
                        tanggal_input = datetime.datetime.strptime(input_tanggal_masuk, "%Y-%m-%d").date()
                        today = datetime.datetime.today().date()
                        if tanggal_input != today:
                            animation("Invalid Data: Harap masukkan tanggal sesuai hari ini", 0.03)
                            continue                        
                        else:
                            break
                    except ValueError:
                        animation("Invalid Input: Format tanggal salah",0.03)
                    

                while True:
                    kategori_penyimpanan = input("Kategori Penyimpanan: ")

                    kategori = True
                    for i in kategori_penyimpanan:
                        if not (i.isalpha() or i == ' '):
                            kategori = False
                            break

                    if kategori and kategori_penyimpanan.strip() != "":
                        break  
                    else:
                        print("Invalid Data: Kategori tidak sesuai")

                while True:
                    kategori_makanan = input("Kategori Makanan: ")
                    valid = True
                    for char in kategori_makanan:
                        if not (char.isalpha() or char == ' '):
                            valid = False
                            break

                    if not valid or kategori_makanan.strip() == "":
                        print("Invalid Data: Kategori Makanan tidak sesuai")
                        continue 

                    break

                No_baru = len(PRODUK) + 1
                PRODUK.append({
                    "no": No_baru,
                    "product_id": input_id,
                    "produk": input_product,
                    "stok": add_stok,
                    "tanggal kadaluarsa": str(input_tanggal_Kadaluarsa),
                    "tanggal masuk": str(input_tanggal_masuk),
                    "kategori penyimpanan": kategori_penyimpanan,
                    "kategori makanan": kategori_makanan
                })
                animation("Produk baru berhasil ditambahkan.",0.03)
                count = len(PRODUK[0])
                print(tabulate(PRODUK, headers='keys', tablefmt='fancy_grid', colalign=('center',) * count))
                return
            
        elif option == 2:
            animation("Mohon tunggu, sedang diproses...", 0.04)
            break
        else: 
            animation("Invalid Input",0.03)

barang_keluar= []        
def product_keluar():
    while True:
         print("-------------------------------------------")
         print("""
    SUB MENU: Outgoing Product
        1. Catat Barang Keluar
        2. Data Barang Keluar
        3. Tambah Tujuan Barang
        4. Kembali ke Menu sebelumnya 
""")
         option = input("Input Menu [1-4]: ")

         if not option.isdigit():
                    print("Invalid Input: ID Product tidak sesuai")
                    continue
         option = int(option)
         if option == 1:
             count = len(PRODUK[0])
             print(tabulate(PRODUK, headers="keys", tablefmt="fancy_grid", colalign=("center",)*count))
             animation("Note: ID Product hanya 4 angka",0.03)
             id_product = input("Input ID Product: ")
             
             if len(id_product) != 4 or not id_product.isdigit():
                    animation("Invalid Input: ID Product tidak sesuai",0.03)
                    continue
             id_product = int(id_product)

             for data in PRODUK:
                 if data["product_id"] == id_product:
                     animation(f"Data {id_product} ditemukan, product {data["produk"]}",0.03)
                     confirm = input(f"Konfirmasi ID Product {id_product} [Yes/No]? ").capitalize()
                     if confirm == "Yes":
                         count = len(PRODUK[0])
                         print(tabulate(PRODUK, headers='keys', tablefmt='fancy_grid', colalign=("center",)*count))
                         product_out = int(input("Input Jumlah Barang: "))
                         if product_out > data["stok"]:
                             animation("Invalid Error: Stok Product tidak cukup",0.03)
                             return
                         
                         data["stok"] -= product_out
                         print(Tujuan_Barang)
                         tujuan = input("Masukkan Tujuan Barang: ")

                         if tujuan.title() not in [t.title() for t in Tujuan_Barang]:
                             print(f"Invalid Data: {tujuan} tidak ada dalam list tujuan barang")
                             return

                         Note = input("Masukkan Deksripsi: ")
                         while True:
                            tanggal_barang_out = input("Input tanggal [yyyy-mm-dd]: ")
                            try:
                                tanggal_barang_out = datetime.datetime.strptime(tanggal_barang_out, "%Y-%m-%d").date()
                                today = datetime.datetime.today().date()
                                if tanggal_barang_out == today:
                                    break
                                else:
                                    animation("Invalid Error: Masukkan tanggal sesuai hari ini",0.03)
                            except ValueError: 
                                animation("Invalid Input: Format tanggal salah",0.03)

                         last_confirm = input("Konfirmasi Barang keluar [Yes/No]: ").capitalize()

                         if last_confirm == "Yes":
                             barang_keluar.append({
                                "product_id": data["product_id"],
                                "produk": data["produk"],
                                "Total": product_out,
                                "Tujuan": tujuan.title(),
                                "Deksripsi": Note,
                                "Tanggal": str(tanggal_barang_out)
                            })
                                
                             count = len(PRODUK[0])
                             print(tabulate(PRODUK, headers='keys', tablefmt='fancy_grid', colalign=('center',)*count))
                             return
             else:
                 animation("ID produk tidak ditemukan",0.03)
         
         elif option == 2:
             if not barang_keluar:
                 animation("Result: Belum ada data barang keluar",0.03)
             else:
                count = len(barang_keluar[0])
                print(tabulate(barang_keluar, headers="keys", tablefmt="fancy_grid", colalign=('center',)*count))
         
         elif option == 3:
             tambah_tujuan_barang = input("Input nama tujuan: ")

             if not tambah_tujuan_barang.isdigit():
                 if tambah_tujuan_barang not in Tujuan_Barang:
                    Tujuan_Barang.append(tambah_tujuan_barang)
                    animation(f"{tambah_tujuan_barang} berhasil ditambahkan...", 0.03)
                 else:
                     animation(f"{tambah_tujuan_barang} sudah ada didaftar", 0.03)
             else: 
                 animation("Invalid Input: Data tidak valid")
         elif option == 4:
             animation("Mohon tunggu, sedang diproses...", 0.04)
             break
         else: 
             animation("Invalid Input: [1-3]",0.03)


def uknown_product():
    while True:
        print("-------------------------------------------")
        print("""
    MENU: Looking For Product?
        1. Cari Produk?
        2. Kembali ke Menu utama 
""")
        option = input("Input Menu [1-2]: ")

        if not option.isdigit():
            animation("Invalid Input: [1-2]",0.03)
            continue

        option = int(option)

        if option == 1:
            try:
                count = len(PRODUK[0])
                print(tabulate(PRODUK, headers='keys', tablefmt='fancy_grid', colalign=("center",)*count))
                animation("Note: ID Product hanya 4 angka",0.03)
                cari_id = input("Input ID Product: ")

                if len(cari_id) != 4 or not cari_id.isdigit():
                    animation("Invalid Input: ID Product tidak sesuai",0.03)
                    continue 

                cari_id = int(cari_id)
                for data in PRODUK:
                    if data["product_id"] == cari_id:
                        animation("Mohon tunggu, sistem sedang mencari...", 0.03)
                        print(f"""
        Produk Ditemukan:
        Product ID        : {data['product_id']}
        Nama Produk       : {data['produk']}
        Stok              : {data['stok']}
        Tanggal Kadaluarsa: {data['tanggal kadaluarsa']}
        Tanggal Masuk      : {data['tanggal masuk']}
        Kategori Penyimpanan: {data['kategori penyimpanan']}
        Kategori Makanan   : {data['kategori makanan']}
                        """)
                        
                        break
                else:
                    animation(f"ID {cari_id} tidak ditemukan",0.03)
                        

            except ValueError:
                animation("Invalid Input: Input [1-2]",0.03)
        
        elif option == 2:
            animation("Mohon tunggu, sedang diproses...", 0.04)
            break
        else:
            animation("Invalid Input: Input[1-2]",0.03)


def expired():
    expired_soon = []  # Menyimpan produk yang sudah difilter
    while True:
        print("-------------------------------------------")
        print("""
    MENU: Status Produk
        1. Filter Produk Kadaluwarsa
        2. Tampilkan Status Produk
        3. Kembali ke Menu utama 
""")
        option = input("Input Menu [1-3]: ")

        if not option.isdigit():
            print("Invalid Input: [1-3]")
            continue

        option = int(option)

        if option == 1:
            hari_ini = datetime.datetime.now().date()
            data_baru = False

            for i in PRODUK:
                kadaluarsa = datetime.datetime.strptime(i["tanggal kadaluarsa"], "%Y-%m-%d").date()
                sisa_hari = (kadaluarsa - hari_ini).days

                if sisa_hari <= 30:
                    # Cek apakah produk sudah difilter
                    sudah_difilter = any(
                        item['product_id'] == i['product_id'] and item['tanggal kadaluarsa'] == i['tanggal kadaluarsa']
                        for item in expired_soon
                    )
                    if sudah_difilter:
                        continue

                    status = "Product Segera Kadaluarsa" if sisa_hari > 0 else "Product Kadaluarsa"
                    animation(f"Data {i['produk']} dengan jumlah stok {i['stok']} {'segera kadaluarsa' if sisa_hari > 0 else 'sudah kadaluarsa'}", 0.04)
                    note = input("Catatan: ")

                    expired_soon.append({
                        "no": len(expired_soon) + 1,
                        "product_id": i["product_id"],
                        "produk": i["produk"],
                        "tanggal kadaluarsa": i["tanggal kadaluarsa"],
                        "Status": status,
                        "Note": note
                    })

                    data_baru = True

            if not data_baru:
                animation("Semua data sudah difilter sebelumnya.", 0.04)

        elif option == 2:
            if not expired_soon:
                animation("Note: Filter Product terlebih dahulu untuk melihat Status Data", 0.04)
            else:
                animation("Data Sedang diproses...", 0.04)
                count = len(expired_soon[0])
                print(tabulate(expired_soon, headers="keys", tablefmt="fancy_grid", colalign=('center',)*count))

        elif option == 3:
            animation("Mohon tunggu, sedang diproses...", 0.04)
            break
        else:
            animation("Invalid Input: [1-3]", 0.04)


def low_product():
    while True:
        print("-------------------------------------------")
        print("""
    SUB MENU: Low Stok
        1. Filter Stok Rendah 
        2. Kembali ke Menu sebelumnya 
""")
        
        option = input("Input Menu [1-3]: ")

        if not option.isdigit():
            animation("Invalid Input: Masukkan Angka [1-3]",0.03)
            continue

        option = int(option)

        if option == 1:
            stok_rendah = [i for i in PRODUK if i["stok"] < 10]

            if not stok_rendah:
                animation("Tidak ada produk dengan stok di bawah 10.\n",0.03)
            else:
                no_baris = [{k: v for k, v in item.items()} for item in stok_rendah]

                animation("Data sedang diproses....", 0.04)
                count = len(no_baris[0])  
                print(tabulate(no_baris, headers="keys", tablefmt="fancy_grid", colalign=("center", )*count, showindex=range(1, len(stok_rendah)+1)))
                print()


        elif option == 2:
            animation("Mohon tunggu, sedang diproses...", 0.04)
            break
        else:
            animation("Invalid Input: Input Menu [1-2]",0.03)

            
def hapus_product():
    while True:
        print("-------------------------------------------")
        print("""
    SUB MENU: Remove Product
        1. Hapus Product 
        2. Kembali ke Menu sebelumnya 
""")
        
        option = input("Input Menu [1-2]: ")

        if not option.isdigit():
            animation("Invalid Input: Masukkan Angka [1-2]",0.03)
            continue

        option = int(option)

        if option == 1:
            try: 
                animation("Data sedang diproses....", 0.04)
                count = len(PRODUK[0])
                print(tabulate(PRODUK, headers="keys", tablefmt="fancy_grid", colalign=('center',)*count))
                id_product = input("Input ID Product: ")

                if len(id_product) == 4 and not id_product.isdigit():
                    animation("Invalid Input ID: ID hanya 4 angka",0.03)
                    continue

                id_product = int(id_product)

                for index, item in enumerate(PRODUK):
                    if item["product_id"] == id_product:
                        confirm = input(f"Apakah anda yakin ingin menghapus produk {item['produk']} dari data [Yes/No]? ").capitalize()
                        if confirm == "Yes":
                            PRODUK.pop(index)
                            animation(f"Produk {item['produk']} berhasil dihapus",0.03)
                            return
                        else:
                            animation("Penghapusan dibatalkan.",0.03)
                            return
                animation(f"ID {id_product} tidak ditemukan",0.03)
            
            except ValueError:
                animation("Invalid tidak valid.",0.03)

        elif option == 2:
            animation("Mohon tunggu, sedang diproses...", 0.04)
            break
        else: 
            animation("Invalid Input: [1-2]",0.03)


while True:
    main_menu()
    option = input("Input Menu [1-6]: ")
    if not option.isdigit():
        animation("Invalid Input: Masukkan Angka [1-6]",0.03)
        continue

    option = int(option)

    if option == 1:
        while True:
            animation("Mohon tunggu, sedang diproses...", 0.04)
            sub_menu()
            opsi1 = input("Input Sub menu [1-4]: ")

            if not opsi1.isdigit():
                animation("Invalid Input: Masukkan Angka [1-4]",0.03)
                continue 
            opsi1 = int(opsi1)

            if opsi1 == 1:
                animation("Mohon tunggu, sedang diproses...", 0.04)
                show_product()
            elif opsi1 == 2:
                animation("Mohon tunggu, sedang diproses...", 0.04)
                product_masuk()
            elif opsi1 == 3:
                animation("Mohon tunggu, sedang diproses...", 0.04)
                product_keluar()
            elif opsi1 == 4:
                animation("Mohon tunggu, sedang diproses...", 0.04)
                break  
            else:
                animation("Invalid Input",0.03)

    elif option == 2:
        animation("Mohon tunggu, sedang diproses...", 0.04)
        uknown_product()  
    elif option == 3:
        animation("Mohon tunggu, sedang diproses...", 0.04)
        expired()
    elif option == 4:
        animation("Mohon tunggu, sedang diproses...", 0.04)
        low_product()
    elif option == 5:
        animation("Mohon tunggu, sedang diproses...", 0.04)
        hapus_product()
    elif option == 6:
        animation("Terima Kasih telah menggunakan program ini....",0.06)
        exit()
    else:
        animation("Invalid Input: Masukkan Angka [1-6]",0.03)



                        
