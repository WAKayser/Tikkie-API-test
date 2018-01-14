def get_tikkie(contacts, auth):
	for key in contacts:
		contacts[key]['link'] = "etv.tudelft.nl"
	return contacts

def tikkie_auth(issuer):
	return'57', '146'

def tikkie_start(auth, api, name, mail, phone, share, iban, label):
	return 3, 3, 3