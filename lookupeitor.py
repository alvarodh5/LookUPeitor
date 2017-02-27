#!/usr/bin/python
# -*- coding: utf-8 -*-
#Autor: Alvaro Diaz Hernandez @alvarodh5
#Contact: alvarodiazher@gmail.com
#Special Thanks to: underc0de.org & fwhibbit.es
#Version 0.1

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
import json
requests.packages.urllib3.disable_warnings()

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def ascii():
	print bcolors.YELLOW + ".____                  __    ____ _____________       .__  __                " + bcolors.ENDC
	print bcolors.YELLOW + "|    |    ____   ____ |  | _|    |   \______   \ ____ |__|/  |_  ___________ " + bcolors.ENDC
	print bcolors.YELLOW + "|    |   /  _ \ /  _ \|  |/ /    |   /|     ___// __ \|  \   __\/  _ \_  __ \ " + bcolors.ENDC
	print bcolors.YELLOW + "|    |__(  <_> |  <_> )    <|    |  / |    |   \  ___/|  ||  | (  <_> )  | \/" + bcolors.ENDC
	print bcolors.YELLOW + "|_______ \____/ \____/|__|_ \______/  |____|    \___  >__||__|  \____/|__|   " + bcolors.ENDC
	print bcolors.YELLOW + "        \/                 \/                       \/                       " + bcolors.ENDC + bcolors.HEADER + "0.1" + bcolors.ENDC
	print bcolors.GREEN + "[-] Coded by Alvaro Diaz Hernandez(@alvarodh5) [-]\n" + bcolors.ENDC


ascii()
if (len(sys.argv) < 3):
	print bcolors.RED+"[!] Enter a valid IP/URL"+bcolors.ENDC
	print bcolors.GREEN+"Ex: python lookupeitor.py --ns 8.8.8.8 "+bcolors.ENDC
	print bcolors.GREEN+"Ex: python lookupeitor.py --ip 8.8.8.8 "+bcolors.ENDC
	print bcolors.BLUE+"[#] Options available:"
	print "	--ns (Reverse Nameserver Lookup)"
	print "	--ip (Reverse IP Lookup)"+bcolors.ENDC
else:
	try:
		url = sys.argv[2]
		ns = False
		ip = False
		
		if ("--ns" in sys.argv):
			print bcolors.BLUE+"[$] Reverse Nameserver Lookup\n"+bcolors.ENDC
			ns = True

		if ("--ip" in sys.argv):
			print bcolors.BLUE+"[$] Reverse IP Lookup\n"+bcolors.ENDC
			ip = True
				
				
		if (ip == True):
			r = requests.get("http://pro.viewdns.info/reverseip/?host="+url+"&apikey=YOURAPIKEYy&output=json")
		else:
			r = requests.get("http://pro.viewdns.info/reversens/?ns="+url+"&apikey=YOURAPIKEYy&output=json")
		
		print bcolors.BLUE+"[*] Analyzing... " + str(url) + bcolors.ENDC
	
		response = r.content
		parsed = json.loads(response)
		print json.dumps(parsed, indent=4, sort_keys=True)

	except requests.exceptions.ConnectionError:
    		print bcolors.YELLOW+"[!] Connection refused, check your proxy or internet connection."+bcolors.ENDC
    	except NameError:
    		print bcolors.RED+"[!] Connection Aborted. Check your options."+bcolors.ENDC
