#!/usr/bin/python

import requests
import fixerCredentials as fxCredentials
from time import strftime, strptime
import datetime
import json





justTime, justDate = strftime("%X"), strftime("%x")
print("\nStarted fx Script on: " + str(justDate) + " at: " + str(justTime) + "\n")








fixerUrl = 'http://data.fixer.io/api/'

#fixerUrl2 = str(str(fixerUrl) + 'latest?access_key=' + str(fxCredz.fixerAPIkey))
#convertUrl = str(str(fixerUrl) + 'convert?access_key=' + str(fxCredz.fixerAPIkey) + '&from=' + str('USD') + '&to=' + str('EUR') + '&amount=' + str(10))
#fixerUrl2 = str(str(fixerUrl) + str('2021-04-23') + '?access_key=' + str(fxCredz.fixerAPIkey))
def getFxRate(baseCurrency, jsonOutAddr):
	baseVar = str("&base=" + str(baseCurrency))

	fixerUrl2 = str(str(fixerUrl) + str('2021-04-23') + '?access_key=' + str(fxCredz.fixerAPIkey) + str(baseVar))



	print("Requesting data from: " + str(fixerUrl2))


	urlRequest = requests.get(fixerUrl2)

	urlResponse = urlRequest.content


	data = json.loads(urlResponse)




	try:
		with open(jsonOutAddr, 'w') as fp1:	json.dump(data, fp1)
		print("\nSuccess Creating FX cache | " + str(len(data)) + " rates processed\n")


	except Exception as e: print(e)


baseCurrency = 'USD'

usdJsonOutAddr = 'data/usd.json'
eurJsonOutAddr = 'data/eur.json'
jpyJsonOutAddr = 'data/jpy.json'
gbpJsonOutAddr = 'data/gbp.json'
cadJsonOutAddr = 'data/cad.json'
audJsonOutAddr = 'data/aud.json'


gfr1 = getFxRate('USD', usdJsonOutAddr)
gfr2 = getFxRate('EUR', eurJsonOutAddr)
gfr3 = getFxRate('JPY', jpyJsonOutAddr)
gfr4 = getFxRate('GBP', gbpJsonOutAddr)
gfr5 = getFxRate('CAD', cadJsonOutAddr)
gfr6 = getFxRate('AUD', audJsonOutAddr)



justTime, justDate = strftime("%X"), strftime("%x")
print("\nFinished fx Script on: " + str(justDate) + " at: " + str(justTime) + "\n")



