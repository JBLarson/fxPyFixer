#! /usr/bin/python

import requests
from datetime import datetime
from time import strftime, strptime, mktime
import dateparser
import json




fxCacheUsdAddr = 'data/usd.json'
fxCacheEurAddr = 'data/eur.json'
fxCacheJpyAddr = 'data/jpy.json'
fxCacheGbpAddr = 'data/gbp.json'
fxCacheCadAddr = 'data/cad.json'
fxCacheAudAddr = 'data/aud.json'


with open(fxCacheUsdAddr, 'r') as f:
	fxCache_usd = json.load(f)

with open(fxCacheEurAddr, 'r') as f:
	fxCache_eur = json.load(f)

with open(fxCacheJpyAddr, 'r') as f:
	fxCache_jpy = json.load(f)

with open(fxCacheGbpAddr, 'r') as f:
	fxCache_gbp = json.load(f)

with open(fxCacheCadAddr, 'r') as f:
	fxCache_cad = json.load(f)

with open(fxCacheAudAddr, 'r') as f:
	fxCache_aud = json.load(f)







justTime, justDate = strftime("%X"), strftime("%x") # needs to be above anything that takes time
print("\n\nStarted Query on: " + str(justDate) + " at: " + str(justTime))






def describeRates(baseCoin, f1, f2):
	bCbFRate = priceRn(str(baseCoin), str(f1))
	bCcFRate = priceRn(str(baseCoin), str(f2))

	#print("\nCoin1: " + str(baseCoin).upper() + "   Fiat1: " + str(f1).upper() + "   Fiat2: " + str(f2).upper())
	print("\nCoin1: " + str(baseCoin).upper())

	crF1 = bCbFRate['lastPrice']
	crF2 = bCcFRate['lastPrice']
	xcF1 = str(str(baseCoin) + '/' + str(f1))
	xcF2 = str(str(baseCoin) + '/' + str(f2))
	print(str(xcF1) + ': ' + str(crF1))
	print(str(xcF2) + ': ' + str(crF2))





# lambda functions for rounding
ro1, ro2, ro4 = lambda x : round(x, 1), lambda x : round(x, 2), lambda x : round(x, 4)


# function to convert DD-MM-YYYY to MM/DD/YYYY
def makeMDY(inputDate):
	dateList = inputDate.split("-")
	outputDate = dateList[1] + "/" + dateList[0] + "/" + dateList[2]

	return outputDate


# function to convert MM/DD/YYYY to DD-MM-YYYY 
def makeDMY(inputDate):
	dateList = inputDate.split("/")
	outputDate = dateList[1] + "-" + dateList[0] + "-" + dateList[2]
	return outputDate


# function to convert unix epoch timestamp to datetime object
def unixOffset(offsetValue):
	startDate = datetime(1970, 1, 1, 0, 0, 0, 0);
	output = datetime.fromtimestamp(int(offsetValue))

	return output







#tezosAts = atStats('tezos', 'usd')
#adaAts = atStats('cardano', 'usd')


def getRates(fxCacheObject):
	base = fxCacheObject['base']
	rates = fxCacheObject['rates']


	isHistorical = fxCacheObject['historical']
	if isHistorical == 'True' or isHistorical == True:
		historicalDate = fxCacheObject['date']
	else:
		historicalDate = 'error fetching historical date'

	cad_b = rates['CAD']
	usd_b = rates['USD']
	jpy_b = rates['JPY']
	eur_b = rates['EUR']
	gbp_b = rates['GBP']
	aud_b = rates['AUD']

	rateResponse = {

		'cad_b': cad_b,
		'usd_b': usd_b,
		'jpy_b': jpy_b,
		'eur_b': eur_b,
		'gbp_b': gbp_b,
		'aud_b': aud_b

	}

	return rateResponse



def describeCurrencies(getRateObject):
	try:
		listOfValues = list(getRateObject.values())
		listOfKeys = list(getRateObject.keys())
		listOfBoth = zip(listOfKeys, listOfValues)
	
		listOfDictItems = getRateObject.items()
		listOfItems = list(listOfDictItems)

		for listItem in listOfDictItems:
			print(listItem)

			try:
				if int(listItem) == 1:
					print("\nIt fucking worked\n")


			except Exception as e:
				print("\nIt failed\n")
				print(e)



	except:
		listOfValues = {'yo': 'failed making the list'}

	print(listOfValues)



	try:

		try:

			fxKeys = getRateObject.keys()
			for fKey in fxKeys:
				print(str(fKey) + ": " + str(getRateObject[fKey]))

		except:
			print("Failed to extract keys")


	except Exception as e:
		print("\nDescribe Currency Function failed bc: " + str(e))

	dcResposnse = """


					Currency: {}  |  {}



				  """.format('JB3', str(getRateObject['usd_b']), str(getRateObject['jpy_b']), str(getRateObject['gbp_b']), str(getRateObject['cad_b']), str(getRateObject['aud_b']))


	return dcResposnse







getEur = getRates(fxCache_eur)
getUsd = getRates(fxCache_usd)
getJpy = getRates(fxCache_jpy)
getGbp = getRates(fxCache_gbp)
getCad = getRates(fxCache_cad)
getAud = getRates(fxCache_aud)



dcEur = describeCurrencies(getEur)
print(dcEur)
dcUsd = describeCurrencies(getUsd)
print(dcUsd)
dcJpy = describeCurrencies(getJpy)
dcGbp = describeCurrencies(getGbp)
dcCad = describeCurrencies(getCad)
dcAud = describeCurrencies(getAud)



justTime, justDate = strftime("%X"), strftime("%x") # needs to be above anything that takes time
print("\nCompleted Query on: " + str(justDate) + " at: " + str(justTime) + "\n\n")

