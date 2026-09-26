# ==========================================
# HOMESTAY - INTERACTIVE ACCOMMODATION PROGRAM
# ==========================================

booking = None  # no booking made yet

homestays = [
    {"name": "KLCC Budget Studio", "state": "Kuala Lumpur", "price": 90, "guests": 2},
    {"name": "Bukit Bintang Family Suite", "state": "Kuala Lumpur", "price": 180, "guests": 5},
    {"name": "Chow Kit Backpacker Room", "state": "Kuala Lumpur", "price": 50, "guests": 1},

    {"name": "Georgetown Heritage Room", "state": "Penang", "price": 80, "guests": 2},
    {"name": "Batu Ferringhi Beach House", "state": "Penang", "price": 220, "guests": 6},
    {"name": "Gurney Drive Studio", "state": "Penang", "price": 100, "guests": 3},

    {"name": "JB City Apartment", "state": "Johor", "price": 70, "guests": 3},
    {"name": "Legoland Family Villa", "state": "Johor", "price": 250, "guests": 6},
    {"name": "Danga Bay Condo", "state": "Johor", "price": 120, "guests": 4},

    {"name": "Jonker Street Heritage Room", "state": "Melaka", "price": 65, "guests": 2},
    {"name": "Melaka River Loft", "state": "Melaka", "price": 110, "guests": 4},
    {"name": "Ayer Keroh Family House", "state": "Melaka", "price": 190, "guests": 6},
]

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
    return states[state_choice]

def make_booking():
    global booking

    selected_state = choose_state()

    pax = int(input("Enter number of guests: "))
    budget = float(input("Enter your budget per night (RM): "))

    #Find matching homestay
    results = []
    for h in homestays:
        if h["state"] == selected_state and h["guests"] >= pax and h["price"] <= budget:
            results.append(h)

    print("\n---Available Homestays---")

    if len(results) == 0:
        print("Sorry, no homestays match your requirements.")
        return

    results.sort(key=lambda x: x["price"])

    for i, h in enumerate(results, start=1):
        print(f"\n{i}. {h['name']}")
        print(f"   Location: {h['state']}")
        print(f"   Guests: Up to {h['guests']}")
        print(f"   Price: RM{h['price']:.2f} per night")

    choice = int(input("\nSelect a homestay (enter number): "))

    if choice < 1 or choice > len(results):
        print("\nInvalid choice.")
        return

    selected = results[choice - 1]
    nights = int(input("\nHow many nights would you like to stay? "))
    total = selected["price"] * nights

    # Booking summary
    print("\n========== BOOKING SUMMARY ==========")
    print(f"Homestay: {selected['name']}")
    print(f"Location: {selected['state']}")
    print(f"Guests: {pax}")
    print(f"Price per night: RM{selected['price']:.2f}")
    print(f"Number of nights: {nights}")
    print(f"Total cost: RM{total:.2f}")

    confirm = input("\nConfirm booking? (Y/N): ").upper()

    if confirm == "Y":
        booking = {
            "name": selected["name"],
            "state": selected["state"],
            "guests": pax,
            "price": selected["price"],
            "nights": nights,
            "total": total
        }

        print("\nBooking confirmed!")
        print("Thank you for using HomeStay!")

    else:
        print("\nBooking cancelled.")

def view_booking():
    if booking is None:
        print("\nYou have no active booking.")
    else:
        print("\n========== YOUR BOOKING ==========")
        print(f"Homestay: {booking['name']}")
        print(f"Location: {booking['state']}")
        print(f"Guests: {booking['guests']}")
        print(f"Price per night: RM{booking['price']:.2f}")
        print(f"Nights: {booking['nights']}")
        print(f"Total cost: RM{booking['total']:.2f}")

def cancel_booking():
    global booking
    if booking is None:
        print("\nYou have no booking to cancel.")
    else:
        print(f"\nBooking for {booking['name']} has been cancelled.")
        booking = None
        

    
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
       make_booking()

    elif choice == "2":
        view_booking()

    elif choice == "3":
        cancel_booking()

    elif choice == "4":
        print("\nExit")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.")


