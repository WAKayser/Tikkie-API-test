from exactreader import get_debts
from dbreader import get_contact
from dummy import tikkie_auth, get_tikkie
from whatsapp import send_all


def main():
	auth = tikkie_auth()
	debts = get_debts()
	data = get_contact(debts)
	data = get_tikkie(data, auth)
	send_all(data)


if __name__ == '__main__':
	main()