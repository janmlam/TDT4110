counter = 1

def logg(name, time, msg):
	global counter
	print ("MSG", counter, ", " + name + " sent this message: " + msg + " at " + time + " o'clock.")
	counter = counter + 1
	return



def main():
	logg("Mr. Y", "23:59", "Har du mottatt pakken?")
	logg("Mdm. Evil", "0:00", "Ja. Pakken er mottatt.")
	logg("Dr. Horrible", "0:03", "All you need is love!")
	logg("Mr. Y", "0:09", "Dr. Horrible, Dr. Horrible , calling Dr. Horrible .")
	logg("Mr. Y", "0:09", "Dr. Horrible, Dr. Horrible wake up now.")
	logg("Dr. Horrible", "0:09", "Up now!")
	return


main()