import datetime


class ATMMachine:

    def __init__(self, initial_balance=0, pin="1234"):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def log_transaction(self, transaction_type, amount=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if transaction_type in ["deposit", "withdraw"]:
            self.transaction_history.append(
                f"{timestamp} - {transaction_type.title()} : ${amount}")
        else:
            self.transaction_history.append(
                f"{timestamp} - {transaction_type.title()}")

    def check_pin(self, pin):
        return pin == self.pin

    def inquire_balance(self):
        self.log_transaction("balance inquiry")
        return self.balance

    def withdraw_cash(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            self.log_transaction("withdraw", amount)
            return f"${amount} withdrawn successfully"

    def deposit_cash(self, amount):
        self.balance += amount
        self.log_transaction("deposit", amount)
        return f"${amount} deposited successfully"

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.log_transaction("pin change")
            return "PIN changed successfully"
        else:
            return "Incorrect old PIN"

    def show_transaction_history(self):
        return "\n".join(
            self.transaction_history
        ) if self.transaction_history else "No transactions yet"


def main():
    atm = ATMMachine(initial_balance=1000)

    print("Welcome to the ATM Machine!")
    pin = input("Enter your PIN: ")

    if not atm.check_pin(pin):
        print("Invalid PIN!")
        return

    while True:
        print("\nMenu:")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            balance = atm.inquire_balance()
            print(f"Your current balance is: ${balance}")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            message = atm.withdraw_cash(amount)
            print(message)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            message = atm.deposit_cash(amount)
            print(message)
        elif choice == "4":
            old_pin = input("Enter your current PIN: ")
            new_pin = input("Enter your new PIN: ")
            message = atm.change_pin(old_pin, new_pin)
            print(message)
        elif choice == "5":
            history = atm.show_transaction_history()
            print("Transaction History:")
            print(history)
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()
