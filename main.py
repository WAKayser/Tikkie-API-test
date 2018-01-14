from exactreader import get_debts
from dbreader import get_contact
from dummy import tikkie_auth, get_tikkie, tikkie_start
from whatsapp import send_all


def main():
	name = 'Wouter Kayser (ETV)'
	mail = '3-etv@tudelft.nl'
	share = False
	phone = '31151781399'
	iban = 'NL51ABNA0603041949'
	label = 'ETV Spaarrekening'

	auth, api = tikkie_auth('Wouter Kayser (ETV)')
	platform, user, bank = tikkie_start(auth, api, name, mail, 
										phone, share, iban, label)
	debts = get_debts()
	data = get_contact(debts)
	data = get_tikkie(data, auth)
	send_all(data)


if __name__ == '__main__':
	main()