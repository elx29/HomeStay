# HomeStay - Affordable Accommodation in Malaysia
# ==========================================

print("=" * 50)
print("              WELCOME TO HomeStay")
print("=" * 50)
print("       Affordable Accommodation in Malaysia")
print()
print("Find a comfortable and affordable place")
print("to stay across Malaysia.")
print("=" * 50)


# Sample homestay data
homestays = [
    {
        "name": "Cozy Kuala Lumpur Stay",
        "state": "Kuala Lumpur",
        "guests": 4,
        "price": 120
    },
    {
        "name": "Family Homestay Selangor",
        "state": "Selangor",
        "guests": 6,
        "price": 150
    },
    {
        "name": "Penang Comfort House",
        "state": "Penang",
        "guests": 4,
        "price": 100
    },
    {
        "name": "Johor Family Apartment",
        "state": "Johor",
        "guests": 5,
        "price": 130
    },
    {
        "name": "Melaka Heritage Homestay",
        "state": "Melaka",
        "guests": 4,
        "price": 110
    }
]


# Stores the user's booking
booking = None


# Search for homestay
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


# View booking
def view_booking():
    print("\n========== VIEW BOOKING ==========")

    if booking is None:
        print("You currently have no booking.")
        return

    print(f"Homestay: {booking['name']}")
    print(f"Location: {booking['state']}")
    print(f"Guests: {booking['guests']}")
    print(f"Price per night: RM{booking['price']:.2f}")
    print(f"Number of nights: {booking['nights']}")
    print(f"Total cost: RM{booking['total']:.2f}")
    print("Booking Status: Confirmed")


# Main Menu
while True:

    print("\nMAIN MENU")
    print("=" * 30)
    print("1. Search for homestay")
    print("2. View Booking")
    print("3. Exit")
    print("=" * 30)

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        search_homestay()

    elif choice == "2":
        view_booking()

    elif choice == "3":
        print("\nThank you for using HomeStay!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 3.")