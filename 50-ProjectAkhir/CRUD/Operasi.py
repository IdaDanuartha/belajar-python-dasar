from . import Database
from .Util import random_str
import time

def create_first_data():
    penulis = input("Penulis : ")
    judul = input("Judul Buku : ")
    tahun = input("Tahun Terbit : ")

    data = Database.TEMPLATE.copy()

    data["id"] = random_str(6)
    data["created_at"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]    
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun

    data_str = f"{data['id']}, {data['penulis']}, {data['judul']}, {data['tahun']}, {data['created_at']}"
    
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal menambahkan data")