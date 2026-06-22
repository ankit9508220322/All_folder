a = int(input("enter the number: "))
match a:
    case 2:
        print("Take a coffee")
    case 5:
        print("Take a food, don’t be lucky")
    case 7:
        print("Good! You’re the winner of an iPhone")
    case _:
        print("Not a valid number")
