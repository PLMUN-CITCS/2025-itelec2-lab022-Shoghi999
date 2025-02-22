while True:
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("Hello! Welcome!")
    elif choice == "2":
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")