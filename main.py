from exactreader import get_debts
from dbreader import get_contact
from dummy import get_tikkie, tikkie_start
from tikkie import tikkie_auth, get_platform
from whatsapp import send_all
from time import sleep


def main():
	name = 'Wouter Kayser (ETV)'
	mail = '3-etv@tudelft.nl'
	share = False
	phone = '31151781399'
	iban = 'NL51ABNA0603041949'
	label = 'ETV Spaarrekening'

	auth, api = tikkie_auth('Wouter Kayser (ETV)')
	print(auth, api)
	sleep(10)
	print(get_platform(auth, api))
	# platform, user, bank = tikkie_start(auth, api, name, mail, 
	# 									phone, share, iban, label)
	# debts = get_debts()
	# data = get_contact(debts)
	# data = get_tikkie(data, auth)
	# send_all(data)


if __name__ == '__main__':
	main()