# KATANA Vs 0,1
from scripts import BruteForceFTP
from scripts import ClientFTP
from scripts import BruteRAR
from scripts import BruteZIP
from scripts import GetDataReport
from scripts import ARPLooking
from scripts import BruteForceFormBase
from scripts import BruteForceHTTP
from scripts import AdminFinder
from core import help
from core import updatekatana


W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'

print """
	   
                  __                         __--
         ___  ___/  \_______________   ___  /  \---
         | .|/ ./ __ \__   ___/.....\  | | / __ \----
         | .  ./ /__\ \/../ _ \. /\..\ | |/ /__\ \-----
         | .| .\.\  /./../ /_\.\.\ \..\| |\.\  /./---
         |_.|\_.\.\/./._/./   \_\.\ \..__| \.\/./--
	    _______?___________________________________
	   {_| | | | I################################/
	      ^ ^ ^ ^             THE FRAMEWORK, VS (0.1)
	   by RedToor

	   """+R+"""Command"""+W+"""\t"""+C+"""Description"""+W+"""
	   help		: help about command
	   show modules	: modules
	   show options : options mudule
	   use		: use module
	   set          : set up 
	   update       : update Katana
	  """

def katana():
	try:
		action = raw_input(B+" KtN> "+W)
		if action == "show modules":
			print "\n 	___________________"
			print "	|web's application|"
			print "	---------------------------------------------"
			print "	|"+O+"web/httpbt"+W+"\t | "+C+"HTTP Brute Force"+W+"        |"
			print "	|"+O+"web/formbt"+W+"\t | "+C+"FORM Brute Force"+W+"        |"
			print "	|"+O+"web/cpfinder"+W+"\t | "+C+"Admin Finder"+W+"            |"
			print "	---------------------------------------------\n 	__________________"
			print "	|sniffing network|"
			print "	---------------------------------------------"
			print "	|"+O+"net/arplook"+W+"\t | "+C+"ARP Attack Detect"+W+"       |"
			print "	---------------------------------------------\n 	___________________"
			print "	|social engineering|"
			print "	---------------------------------------------"
			print "	|"+O+"seng/gdreport"+W+"\t | "+C+"Getting information"+W+"     |"
			print "	---------------------------------------------\n 	______"
			print "	|files|"
			print "	---------------------------------------------"
			print "	|"+O+"file/brutezip"+W+"\t | "+C+"ZIP Brute Force"+W+"         |"
			print "	|"+O+"file/bruterar"+W+"\t | "+C+"RAR Brute Force"+W+"         |"
			print "	---------------------------------------------\n 	_________"
			print "	|Clients|"
			print "	---------------------------------------------"
			print "	|"+O+"clt/ftp"+W+"\t | "+C+"FTP Client"+W+"              |"
			print "	---------------------------------------------\n 	_________"
			print "	|Brute Force Protocols|"
			print "	---------------------------------------------"
			print "	|"+O+"bt/ftp"+W+"\t 	 | "+C+"FTP Brute Force"+W+"         |"
			print "	---------------------------------------------"
			katana()
		elif action[0:3] == "use":
			if action[4:14] == "web/httpbt":
				BruteForceHTTP.httpbt()
			if action[4:16] == "web/cpfinder":
				AdminFinder.adminfinder()
			if action[4:16] == "web/formbt":
				BruteForceFormBase.httpformbasebruteforce()
			if action[4:16] == "net/arplook":
				ARPLooking.arplook()
			if action[4:17] == "seng/gdreport":
				GetDataReport.getdatareport()
			if action[4:17] == "file/brutezip":
				BruteZIP.btzip()
			if action[4:17] == "file/bruterar":
				BruteRAR.btRAR()
			if action[4:11] == "clt/ftp":
				ClientFTP.cftp()
			if action[4:10] == "bt/ftp":
				BruteForceFTP.btftp()
			else:
				katana()
		elif action == "exit":
			print C+"   GooD"+W+" bye."
			exit()
		elif action == "help":
			help.help()
		elif action == "update":
			updatekatana.update()
		else:
			print "[!] command No "+O+"ACCEPT"+W
	except(KeyboardInterrupt, SystemExit):
		print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
katana()