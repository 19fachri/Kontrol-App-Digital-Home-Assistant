import RPi.GPIO as GPIO

class AirCOnditioner(object):
	sinyal="mati"
	def __init__ (self):
		print "konstraktor AirConditioner"
		# GPIO.setmode(GPIO.BCM)
		# GPIO.setup(16, GPIO.OUT)
	# def kendali (self,s):
	# 	if s == "hidup":
	# 		GPIO.output(16, GPIO.HIGH)
	# 		return "sukses"
	# 	elif s == "mati":
	# 		GPIO.output(16, GPIO.LOW)
	# 		return "sukses"
	# 	else : 
	# 		return "gagal"
