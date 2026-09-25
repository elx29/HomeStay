# ==========================================
# HOMESTAY - INTERACTIVE ACCOMMODATION PROGRAM
# ==========================================

print("=" * 50)
print("              WELCOME TO HomeStay")
print("=" * 50)
print("       Affordable Accommodation in Malaysia")
print()
print("Find a comfortable and affordable place")
print("to stay across Malaysia.")
print("=" * 50)

while True:

    print("\nMAIN MENU")
    print("=" * 30)
    print("1. Choose a state:")
    print("2. Enter number of pax:")
    print("3. Enter your budget per night(RM):")
    print("4. Exit")
    print("=" * 30)

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nYou selected Choose a state.")

    elif choice == "2":
        print("\nYou selected Enter number of pax.")

    elif choice == "3":
        print("\nYou selected Enter your budget per night(RM).")

    elif choice == "4":
        print("\nThank you for using HomeStay!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.")