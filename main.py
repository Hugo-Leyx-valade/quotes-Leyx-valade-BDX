from functions import *


def menu():
	print("\n==== Programming Quotes ====")
	print("1. Random quote")
	print("2. Display quotes")
	print("3. Exit")
	print("2. All quotes")
    print("3. Add quote")
	print("4. Exit")



def main():
	while True:

		quotes = load_quotes("quotes.txt")
		menu()

		choice = input("Choose your an action (1-3): ")

		if choice == "1":
			print_quote(random_quote(quotes))
		elif choice == "2":

			count = int(input("Saisir le nombre de quotes à afficher"))
			display_quote(quotes,count)
		elif choice == "3":
			view_quotes(quotes)
        elif choice == "3":
            add_quote(quotes,"quotes.txt")
		elif choice == "4":
			print("Good bye...")
			break
		else:
			print("Invalid input")


if __name__ == "__main__":
	main()
