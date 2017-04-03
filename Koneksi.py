import MySQLdb
class Koneksi(object):
	
	perintah="kosong"
	
	def __init__(self):
		self.db = MySQLdb.connect("localhost","root","1nt3rn3t","DigitalHomeAssistant")
	def start(self):
		self.cursor = self.db.cursor()
	def stop(self):
		self.db.close()
	def getPerintah(self):
		sql = "select kata from List"
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		if data is not None:
			Koneksi.perintah = data[0]
			sql = "delete from List limit 1"
			self.cursor.execute(sql)
			self.db.commit()
			return Koneksi.perintah
		else:
			Koneksi.perintah = "kosong"
			return Koneksi.perintah
	def getKategori(self):
		sql = "select id_alat from Aktivitas where perintah = '%s'" % (Koneksi.perintah)
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		if data is not None:
			return data[0]
		else:
			return "kosong"
	def getStatus(self):
		sql = "select sinyal from Aktivitas where perintah = '%s'" %(Koneksi.perintah)
		self.cursor.execute(sql)
		data = self.cursor.fetchone()
		if data is not None:
			return data[0]
		else:
			return "gagal"
	def saveHistory(self,s):
		sql= "insert into Status value('%s')" % (s)
		self.cursor.execute(sql)
		self.db.commit()
