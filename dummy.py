def get_tikkie(contacts, auth):
	for key in contacts:
		contacts[key]['link'] = "etv.tudelft.nl"
	return contacts

def tikkie_auth():
	return'200'