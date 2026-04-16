

balance = int(input("Enter your starting balance: ₹"))

print("\n--- Bank Menu ---")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = input("Enter choice: ")

if choice == "1":
    print("Balance is:", balance)

elif choice == "2":
    amount = int(input("Enter amount: "))
    if amount > 0:
        balance = balance + amount
        print("Money deposited")
        print("Updated Balance:", balance)  
    else:
        print("Invalid amount")

elif choice == "3":
    amount = int(input("Enter amount: "))
    if amount > balance:
        print("Not enough balance")
    else:
        balance = balance - amount
        print("Money withdrawn")
        print("Updated Balance:", balance)   

elif choice == "4":
    print("Thank you!")

else:
    print("Wrong choice")