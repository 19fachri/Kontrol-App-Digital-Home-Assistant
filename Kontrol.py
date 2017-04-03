import time
from Koneksi import Koneksi
from Lampu import Lampu
from Television import Television
from AirConditioner import AirConditioner

class Kontrol:
	def utama():
		lampu = Lampu()
		Television = Television()
		AirConditioner = AirConditioner()
		while True:
			hasil = "gagal"
			konek = Koneksi()
			konek.start()
			data = konek.getPerintah()
			if data is not "kosong":
				kategori = konek.getKategori();
				if kategori==1:
					hasil = lampu.kendali(konek.getStatus())
				elif kategori==2:
					print "untuk TV"
				elif kategori==3:
					print "untuk AC"
				else :
					hasil = "belum terdaftar"
				respon =  "perintah "+data+" "+hasil
#				konek.saveHistory(respon)
				print respon
			konek.stop()
			time.sleep(1)
	utama()
