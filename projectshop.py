import os
import getpass
import csv 
import datetime as dt

pesanan = [] #list kosong untuk pesanan
jumlah = [] #list kosong jumlah pesanan
hargap= [] #list harga total beberapa pesanan
jenisp = [] #list jenis pesanan
brandp = [] #list brand pesanan
kondisip = [] #list kondisi pesanan
barang = ["rtx", "gtx"]  #list barang yang ditampilkan di menu penjualan
jenis = ["VGA","VGA"] #list jenis yang ditampilkan di menu penjualan
brand = ["Asus", "MSI"] #list brand yang ditampilkan di menu penjualan
kondisi = ["baru","bekas"] #list kondisi yang ditampilkan di menu penjualan 
harga =[10000, 2000] #list harga barang yang ditampilkan di menu penjualan
user = [] #list data user untuk login
no = [] #List no telepon user
alamat = [] #list alamat user
username = ["online"] #list username user
password = ["online123"] #list password user 

def clear():
    os.system("cls")

def garis ():
    print ('='* 96)

def cover ():
    garis()
    print (r""" 
     ___   ___      ___   _  _______  __   __    _______  _______  _______  ______    _______ 
    |   | |   |    |   | | ||       ||  |_|  |  |       ||       ||       ||    _ |  |       |
    |   | |   |    |   |_| ||   _   ||       |  |  _____||_     _||   _   ||   | ||  |    ___|
    |   | |   |    |      _||  | |  ||       |  | |_____   |   |  |  | |  ||   |_||_ |   |___ 
    |   | |   |___ |     |_ |  |_|  ||       |  |_____  |  |   |  |  |_|  ||    __  ||    ___|
    |   | |       ||    _  ||       || ||_|| |   _____| |  |   |  |       ||   |  | ||   |___ 
    |___| |_______||___| |_||_______||_|   |_|  |_______|  |___|  |_______||___|  |_||_______|
""")
    garis()

def enter():
    enter = input ("tekan [ENTER] untuk melanjutkan")
    
def readlogin ():
    users = {}
    with open ("login.csv", mode = "r") as file :
        csv_reader = csv.DictReader(file)
        for row in csv_reader :
            users[row["username"]] = row ["password"]
    return users

def awal ():
    clear()
    cover()
    print ("""
menu pilihan :
    1. registrasi
    2. login
""")
    inputuser = input ("masukkan pilihan >>")
    if inputuser == "1":
        regist()
    elif inputuser == "2":
        login ()

def regist ():
    print ("menu registrasi ")
    username = input ("buat username baru >>")
    password = input ("buat password baru >>")
    with open ("login.csv", mode = "a", newline = "\n") as file :
        border = ["username", "password"]
        writer = csv.DictWriter(file, fieldnames=border)
        tulis = ({"username" : username, "password" : password})
        writer.writerow(tulis)
    print ("anda berhasil melakukan registrasi, silahkan melakukan login ulang")
    enter ()
    awal()

def login ():
    users = readlogin()
    username = input ("masukkan username anda >> ")
    password = input ("masukkan password anda >> ")
    if username in users and password in users[username] :
        menu()
    else : 
        print ("username dan password anda tidak terdaftar, silahkan lakukan registrasi atau ")
        login()
def menu ():
    clear()
    cover()
    print ("""
Main Menu : 
    1. Jual Barang
    2. Beli Barang
    3. Keranjang Pesanan
    4. Pembayaran 
    5. Log out
""")
    pilihan = input ("masukkan menu pilihan >>")
    if pilihan == "1":
        enter()
        jual ()
    elif pilihan == "2":
        enter()
        beli ()
    elif pilihan == "3":
        enter()
        keranjang ()
    elif pilihan == "4":
        enter()
        bayar ()
    elif pilihan == "5":
        enter()
        print ("terimasih telah menggunakan program")
        awal()
    else :
        enter()
        print ("menu tidak tersedia, silahkan pilih kembali")
        menu()

    
def jual ():
    clear()
    cover()
    jenisk = input("masukkan jenis komponen yang akan anda jual >>")
    brandk = input("masukkan brand komponen yang akan anda jual >>")
    jualbarang = input ("masukkan seri komponen yang ingin di jual >>")
    kondisik = input ("baru atau bekas >>")
    hargajual  = int (input("tentukan harga barang yang ingin anda jual >>"))
    jenis.append(jenisk)
    brand.append(brandk)
    barang.append(jualbarang)
    kondisi.append(kondisik)
    harga.append(hargajual)
    print (f"berasil menginpu ke menu penjualan ")
    enter()
    menu()

def beli():
    clear()
    cover()
    border = ["no", "Jenis Komponen", "Brand", "Seri","Kondisi","Harga"]
    print ("="*96)
    print (f"|{border[0]:<3}|{border[1]:<15}|{border[2]:<15}|{border[3]:<26}|{border[4]:<15}|{border[5]:<15}|")
    print ("="*96)
    for x in range (len(barang)):
        print (f"|{x+1:<3}|{jenis[x]:<15}|{brand[x]:<15}|{barang[x]:<26}|{kondisi[x]:<15}|{harga[x]:<15}|")
        print ("-"*96)
    
    pesan = int(input ("masukkan no barang yang ingin di pilih >>"))
    barangp = barang[pesan - 1]
    jumlahp = int (input("berapa jumlah barang yang ingin anda beli >>"))
    harga1 = harga[pesan -1] * jumlahp
    jenis1 = jenis[pesan-1]
    brand1 = brand[pesan-1]
    kondisi1 = kondisi[pesan-1]
    pesanan.append(barangp)
    jumlah.append(jumlahp)
    hargap.append(harga1)
    jenisp.append(jenis1)
    brandp.append(brand1)
    kondisip.append(kondisi1)
    print ("pesanan telah masuk ke keranjang anda")
    enter()
    menu ()

def keranjang():
    clear()
    cover()
    print ("keranjang belanja :")
    border = ["no", "Jenis Komponen", "Brand", "Seri","Kondisi","jumlah","Harga"]
    print ("="*96)
    print (f"|{border[0]:<3}|{border[1]:<15}|{border[2]:<10}|{border[3]:<20}|{border[4]:<15}|{border[5]:<11}|{border[6]:<13}|")
    print ("="*96)
    for x in range (len(jenisp)):
        print (f"|{x+1:<3}|{jenisp[x]:<15}|{brandp[x]:<10}|{barang[x]:<20}|{kondisip[x]:<15}|{jumlah[x]:<11}|{hargap[x]:<13}|")
        print ("-"*96)

    print ("""
1. kembali ke menu
2. lanjutkan ke pembayaran
3. hapus barang
""")
    pilih = int (input(">>"))
    if pilih == 1 :
        enter()
        menu()
    elif pilih == 2 :
        enter ()
        bayar()
    elif pilih == 3 :
        x = int(input ("barang ke berapa yang akan dihapus >>"))
        pesanan.pop(x-1)
        jumlah.pop(x-1)
        hargap.pop(x-1)
        jenisp.pop(x-1)
        brandp.pop(x-1)
        kondisip.pop(x-1)

        print (f"barang telah terhapus")
        enter()
        menu()
    else :
        print ("opsi tidak tersedia ")
        enter()
        keranjang ()

def bayar():
    clear()
    cover()
    print("rincian barang :")
    border = ["no", "Jenis Komponen", "Brand", "Seri","Kondisi","jumlah","Harga"]
    print ("="*96)
    print (f"|{border[0]:<3}|{border[1]:<15}|{border[2]:<10}|{border[3]:<20}|{border[4]:<15}|{border[5]:<11}|{border[6]:<13}|")
    print ("="*96)
    for x in range (len(jenisp)):
        print (f"|{x+1:<3}|{jenisp[x]:<15}|{brandp[x]:<10}|{barang[x]:<20}|{kondisip[x]:<15}|{jumlah[x]:<11}|{hargap[x]:<13}|")
        print ("-"*96)
    print ("""
menu : 
    1. kembali ke menu 
    2. kembali ke keranjang
    3. pilih metode pembayaran 
""")
    pilihan = int(input(">>"))
    if pilihan == 1 :
        enter ()
        menu ()
    elif pilihan == 2 :
        enter ()
        keranjang()
    elif pilihan == 3 :
        print ("""
1. Bayar di tempat (COD)
2. pembayaran secara online (transfer)
""")
        bayar = int (input (">>"))
        if bayar == 1:
            cod = 5000
            hargap.append(cod)
            enter()
            clear()
            cover()
            print (f"tanggal : {dt.date.today()}")
            print (f"waktu : {dt.time()}")
            border = ["no", "Jenis Komponen", "Brand", "Seri","Kondisi","jumlah","Harga"]
            print ("="*96)
            print (f"|{border[0]:<3}|{border[1]:<15}|{border[2]:<10}|{border[3]:<20}|{border[4]:<15}|{border[5]:<11}|{border[6]:<13}|")
            print ("="*96)
            for x in range (len(jenisp)):
                print (f"|{x+1:<3}|{jenisp[x]:<15}|{brandp[x]:<10}|{barang[x]:<20}|{kondisip[x]:<15}|{jumlah[x]:<11}|{hargap[x]:<13}|")
                print ("-"*96)
            print ("="*96)
            print (f"| Biaya COD                                                                    |{cod:<15}|")
            print (f"| TOTAL                                                                        |{sum(hargap):<15}|")
            print ("="*96)
            
        if bayar == 2:
            enter()
            clear()
            cover()
            print (f"tanggal : {dt.date.today()}")
            print (f"waktu : {dt.date.today()}")
            border = ["no", "Jenis Komponen", "Brand", "Seri","Kondisi","jumlah","Harga"]
            print ("="*96)
            print (f"|{border[0]:<3}|{border[1]:<15}|{border[2]:<10}|{border[3]:<20}|{border[4]:<15}|{border[5]:<11}|{border[6]:<13}|")
            print ("="*96)
            for x in range (len(jenisp)):
                print (f"|{x+1:<3}|{jenisp[x]:<15}|{brandp[x]:<10}|{barang[x]:<20}|{kondisip[x]:<15}|{jumlah[x]:<11}|{hargap[x]:<13}|")
                print ("-"*96)
            print ("="*96)
            print (f"| TOTAL                                                                        |{sum(hargap):<15}|")
            print ("="*96)
            
        
if __name__ == "__main__":
    awal ()


