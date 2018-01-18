from exactreader import get_debts
from dbreader import get_contact
from tikkie import *
from whatsapp import send_all


def sent_tikkies():
	limit = 100
	offs = 0
	auth, api = tikkie_auth('Wouter Kayser (ETV)')
	platform = get_platform(auth, api)
	data = get_user(auth, api, platform)
	user, bank = data['userToken'], data['bankAccounts'][0]['bankAccountToken']
	print(get_payments(auth, api, platform, user, offs, limit))


def main():
	name = 'ETV'
	mail = '3-etv@tudelft.nl'
	share = False
	phone = '0681606186'
	iban = 'NL51ABNA0603041949'
	label = 'ETV Spaarrekening'

	auth, api = tikkie_auth('Wouter Kayser (ETV)')
	# print('auth, api', auth, api)

	# print(post_platform(auth, api, name, phone, mail))
	platform = get_platform(auth, api)
	# print('platform', platform)

	# user, bank = post_user(auth, api, platform, name, phone, iban, label)
	# print('user, bank', user, bank)

	data = get_user(auth, api, platform)
	user, bank = data['userToken'], data['bankAccounts'][0]['bankAccountToken']
	# print('user, bank', user, bank)

	debts = get_debts()
	data = get_contact(debts)
	data = get_tikkie(data, auth, api, platform, user, bank)
	send_all(data)


if __name__ == '__main__':
	main()
