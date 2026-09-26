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

    choice = input("Enter your choice (1-3): ")

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
        print("\nInvalid choice. Please enter a number from 1 to 3.")


    def search_homestay():
    global booking

    print("\n========== SEARCH FOR HOMESTAY ==========")

    print("\nChoose a state:")
    print("1. Kuala Lumpur")
    print("2. Selangor")
    print("3. Penang")
    print("4. Johor")
    print("5. Melaka")

    state_choice = input("\nEnter your choice: ")

    states = {
        "1": "Kuala Lumpur",
        "2": "Selangor",
        "3": "Penang",
        "4": "Johor",
        "5": "Melaka"
    }

    if state_choice not in states:
        print("\nInvalid choice.")
        return

    selected_state = states[state_choice]

    # Number of guests
    guests = int(input("\nNumber of guests: "))

    # Budget
    budget = float(input("Budget per night (RM): "))

    # Find suitable homestays
    results = []

    for homestay in homestays:
        if (
            homestay["state"] == selected_state
            and homestay["guests"] >= guests
            and homestay["price"] <= budget
        ):
            results.append(homestay)

    # Display results
    print("\n========== AVAILABLE HOMESTAYS ==========")

    if len(results) == 0:
        print("Sorry, no homestays match your requirements.")
        return

    for i, homestay in enumerate(results, start=1):
        print(f"\n{i}. {homestay['name']}")
        print(f"   Location: {homestay['state']}")
        print(f"   Guests: Up to {homestay['guests']}")
        print(f"   Price: RM{homestay['price']:.2f} per night")

    # Select homestay
    choice = int(input("\nSelect a homestay: "))

    if choice < 1 or choice > len(results):
        print("\nInvalid choice.")
        return

    selected = results[choice - 1]

    # Number of nights
    nights = int(input("\nHow many nights would you like to stay? "))

    total = selected["price"] * nights

    # Booking summary
    print("\n========== BOOKING SUMMARY ==========")
    print(f"Homestay: {selected['name']}")
    print(f"Location: {selected['state']}")
    print(f"Guests: {guests}")
    print(f"Price per night: RM{selected['price']:.2f}")
    print(f"Number of nights: {nights}")
    print(f"Total cost: RM{total:.2f}")

    confirm = input("\nConfirm booking? (Y/N): ").upper()

    if confirm == "Y":
        booking = {
            "name": selected["name"],
            "state": selected["state"],
            "guests": guests,
            "price": selected["price"],
            "nights": nights,
            "total": total
        }

        print("\nBooking confirmed!")
        print("Thank you for using HomeStay!")

    else:
        print("\nBooking cancelled.")