import time
from Koneksi import Koneksi
from Lampu import Lampu

class Kontrol:
	def utama():
		lampu = Lampu()
		while True:
			hasil = "gagal"
			konek = Koneksi()
			konek.start()
			data = konek.getPerintah()
			if data is not "kosong":
				if konek.getKategori()==1:
					hasil = lampu.kendali(konek.getStatus())
				else :
					hasil = "belum terdaftar"
				respon =  "perintah "+data+" "+hasil
#				konek.saveHistory(respon)
				print respon
			konek.stop()
			time.sleep(1)
	utama()
