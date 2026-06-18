
menu = input(""" 
Hi, I can help you
1. enter 1 for pin change
2. enter 2 for forgot pin
3. enter 3 for check balance
4. enter 4 for withdrawal 
5. enter 5 for exit
""")

if menu == '1':
    A = input("Enter the card number: ")
    print(f"{A} change the pin")

elif menu == '2':
    print("Forgot pin")

elif menu == '3':
    print("Check balance")

elif menu == '4':
    print("Withdraw money")

elif menu == '5':
    print("Exit the menu")

else:
    print("Invalid choice")
    menu()
# help('modules')