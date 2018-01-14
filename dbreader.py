from csv import reader

def read_db():
	info = {}
	with open('Debcode.csv', 'r') as file:
		file.readline()
		data = reader(file, delimiter=";", quotechar="\"")
		for row in data:
			if row[2]:
				info[row[0]] = {'name': row[1], 'phone': row[2][1:].replace(' ', '')}
	return info


def get_contact(debts):
	contacts = {}
	info = read_db()
	for code, debt in debts.items():
		try:
			contacts[code] = info[code]
			contacts[code]['debt'] = debt
		except:
			pass
	return contacts		
