# ==========================================
# HOMESTAY - INTERACTIVE ACCOMMODATION PROGRAM
# ==========================================


def choose_state():
    states = {
        "K": "Kuala Lumpur",
        "P": "Penang",
        "J": "Johor",
        "M": "Melaka"
    }

    print("\n---Choose a state to stay in---")
    print("K - Kuala Lumpur")
    print("P - Penang") 
    print("J - Johor")
    print("M - Melaka")

    state_choice = input("Enter your choice (K/P/J/M): ").upper()

    while state_choice not in states:
        print("Invalid choice. Please enter K, P, J, or M.")
        state_choice = input("Enter your choice (K/P/J/M): ").upper()

    print()
    print(f"You selected {states[state_choice]}.")
    return state_choice


    
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
    print("1. Make a booking")
    print("2. View your booking")
    print("3. Cancel booking")
    print("4. Exit")
    print("=" * 30)

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nMake a booking.")
        selected_state = choose_state()

    elif choice == "2":
        print("\nView your booking.")

    elif choice == "3":
        print("\nCancel booking")

    elif choice == "4":
        print("\nExit")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.")