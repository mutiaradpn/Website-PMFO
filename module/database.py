from datetime import date,datetime
import math
import numpy as np
import pymysql
from joblib import Parallel, delayed 
import joblib
import pandas as pd

class Database:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", database="optik", charset='utf8mb4')
    
    def login(self, req):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM akun where username = '"+req['username']+"'")
            con.commit()
            if(cursor.rowcount>0):
                kursor = cursor.fetchall()
                print(kursor)
                if(kursor[5] == req["password"]):
                    return kursor
                else:
                    return "salah password"
            else:
                return "username tidak tersedia"
        except:
            return "error ketika login"
        finally:
            con.close()
            
    def register(self, req):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("insert into akun(username,email,namadepan,namabelakang,password) values('"+req['username']+"','"+req['email']+"','"+req['namadepan']+"','"+req['namabelakang']+"','"+req['password']+"')")
            con.commit()
            if(cursor.rowcount==1):
                return "terisi"
            else:
                return "kosong"
        except:
            return "kosong"
        finally:
            con.close()
            
    def masukin_BER(self, req):
        con = Database.connect(self)
        cursor = con.cursor()
        model = joblib.load('module/model.pkl')
        
        try:
            # Ambil tanggal hari ini
            tanggal = datetime.now()
            
            # Ambil nilai osnr dan ber dari request
            osnr = float(req['osnr'])
            kanal = int(math.floor(eval(req['kanal'])))
            spasi_kanal = int(math.floor(eval(req['spasi'])))
            power = int(math.floor(eval(req['power'])))
            panjang =  int(math.floor(eval(req['panjang'])))
            redaman = float(req['redaman'])
            q_factor = float(req['qfactor'])
            
            # Prediksi nilai berdasarkan model
            data = np.array([{"kanal":kanal, "spasi_kanal_(ghz)":spasi_kanal,	"power_(dbm)":power,"panjang_kabel_(km)":panjang,"redaman_(dbm/km)":redaman,"osnr_(db)": osnr,'q_factor':q_factor}])
            df = pd.DataFrame.from_records(data)
            hasilprediksi = model.predict(df)
            if(hasilprediksi[0] == 0):
                hasil = "optimal"
            elif(hasilprediksi[0] == 1):
                hasil = "repairing"
            else:
                hasil = "maintenance"
            # Masukkan data ke dalam database menggunakan parameterized query
            cursor.execute("INSERT INTO inputber (tanggal, kanal,spasi_kanal,panjang,power,qfactor,redaman, osnr, hasil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (tanggal, kanal,spasi_kanal,panjang,power,q_factor,redaman, osnr, hasil))
            con.commit()
            
            # Periksa apakah operasi insert berhasil
            if cursor.rowcount == 1:
                return hasil
            else:
                return "error"
        
        except Exception as e:
            # Tangkap dan kembalikan pesan kesalahan jika ada
            return "Error: " + str(e)
        
        finally:
            # Selalu pastikan untuk menutup koneksi setelah selesai
            con.close()
            
    def readhistory(self):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("""
            SELECT id,substring(tanggal, 1, 19) as formatted_date,kanal,spasi_kanal,panjang,power,qfactor,redaman,osnr,hasil
            FROM inputber 
            ORDER BY STR_TO_DATE(LEFT(tanggal, 19), '%Y-%m-%d %H:%i:%s') DESC""")
            
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()