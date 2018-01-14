from csv import reader
from collections import defaultdict

def all_debt_codes():
	with open('FintransactionSearch(1).csv', 'rb') as fi:
		fi.readline()
		data = fi.read()
	with open('FintransactionSearch(1).csv', 'wb') as fo:
		fo.write(data.replace(b'\x00', b''))

	totals = {}

	with open("FintransactionSearch(1).csv" , 'r') as file:
		data = reader(file, delimiter="\t", quotechar="\"")
		for row in data:
			code = row[6][-4:]
			change = float(row[8].replace('.','').replace(',','.'))
			totals[code] = round(totals.get(code, 0) + change, 2)

	return(totals)

def get_debts():
	totals = all_debt_codes()
	debts = {}
	for code, debt in totals.items():
		if debt > 0:
			debts[code] = debt
	return debts
