# main.py
import bankcore
import accounts

def main():
    while True:
        print("\n=== Banking Application ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter your name: ").strip()
            user_id = input("Choose a username: ").strip()
            password = input("Choose a password: ").strip()

            cust_id = bankcore.create_account(name, user_id, password)
            accounts.balance_record[cust_id] = 0  # initialize balance

        elif choice == "2":
            cust_id = input("Enter your Customer ID: ").strip()
            password = input("Enter your Password: ").strip()

            if bankcore.login(cust_id, password):
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    option = input("Enter your choice: ").strip()

                    if option == "1":
                        accounts.check_balance(cust_id)
                    elif option == "2":
                        amount = float(input("Enter deposit amount: "))
                        accounts.deposit(cust_id, amount)
                    elif option == "3":
                        amount = float(input("Enter withdrawal amount: "))
                        accounts.withdraw(cust_id, amount)
                    elif option == "4":
                        print("\nLogging out...")
                        break
                    else:
                        print("\nInvalid option!")

        elif choice == "3":
            print("\nExiting the application...")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
