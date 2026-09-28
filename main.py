# ==========================================
# HOMESTAY - INTERACTIVE ACCOMMODATION PROGRAM
# ==========================================

booking = []  # no booking made yet

homestays = [
    {"name": "Convenient stay on KLCC ", "state": "Kuala Lumpur", "price": 77, "guests": 2},
    {"name": "Reunion Loft @ Cheras", "state": "Kuala Lumpur", "price": 175, "guests": 6},
    {"name": "Opus KL", "state": "Kuala Lumpur", "price": 190, "guests": 8},
    {"name": "Central Stay @ Dua Sentral", "state": "Kuala Lumpur", "price": 130, "guests": 4},
    {"name": "Chow Kit Backpacker Room", "state": "Kuala Lumpur", "price": 50, "guests": 1},
    {"name": "Modern Studio @ Liberty", "state": "Kuala Lumpur", "price": 100, "guests": 2},

    {"name": "City Town Apartment in Georgetown ", "state": "Penang", "price": 165, "guests": 3},
    {"name": "Unesco Core", "state": "Penang", "price": 40, "guests": 1},
    {"name": "Simple Urban Suites", "state": "Penang", "price": 250, "guests": 8},
    {"name": "Condo In Georgetown", "state": "Penang", "price": 335, "guests": 6},
    {"name": "Minden Height 5", "state": "Penang", "price": 100, "guests": 1},

    {"name": "1 Bed Studio", "state": "Johor", "price": 130, "guests": 2},
    {"name": "Legoland View Apartment in Iskandar Puteri", "state": "Johor", "price": 170, "guests": 2},
    {"name": "ValueRoomz SouthKey MidVallyey", "state": "Johor", "price": 55, "guests": 1},
    {"name": "The Gardence Residence Apartment", "state": "Johor", "price": 200, "guests": 4},
    {"name": "Seaview Luxury Suite @ Danga Bay", "state": "Johor", "price": 500, "guests": 6},

    
    {"name": "Jonker Street Heritage Room", "state": "Melaka", "price": 65, "guests": 2},
    {"name": "GuestHouse Single Room", "state": "Melaka", "price": 45, "guests": 1},
    {"name": "Seaview Studio Bathtub @ Imerio Melaka", "state": "Melaka", "price": 110, "guests": 2},
    {"name": "Signature High Floor 4pax Suite @The Pines Melaka", "state": "Melaka", "price": 105, "guests": 4},
    {"name": "Jonker Riverwalk Townhouse", "state": "Melaka", "price": 290, "guests": 8},
    
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

    pax = int(input("Enter number of guests (Maximum 8): "))
    while pax < 1 or pax > 8:
        print("Sorry, we don't provide rooms for that many guests yet. We currently support up to 8 guests.")
        pax = int(input("Enter number of guests (Maximum 8): "))

    budget = float(input("Enter your budget per night (RM): "))
    while budget <= 0:
        print("Invalid budget. Please enter a positive number.")
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

    def get_price(homestay):
        return homestay["price"]

    results.sort(key=get_price)

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
        booking.append({
            "name": selected["name"],
            "state": selected["state"],
            "guests": pax,
            "price": selected["price"],
            "nights": nights,
            "total": total
        })

        print("\nBooking confirmed!")
        print("Thank you for using HomeStay!")

    else:
        print("\nBooking cancelled.")

def view_booking():
    if len(booking) == 0:
        print("\nYou have no active booking.")
    else:
        print("\n========== YOUR BOOKING ==========")
        for i, b in enumerate(booking, start=1):
            print(f"\nBooking {i}:")
            print(f"Homestay: {b['name']}")
            print(f"Location: {b['state']}")
            print(f"Guests: {b['guests']}")
            print(f"Price per night: RM{b['price']:.2f}")
            print(f"Nights: {b['nights']}")
            print(f"Total cost: RM{b['total']:.2f}")

def cancel_booking():
    
    if len(booking) == 0:
        print("\nYou have no booking to cancel.")
        return

    print("\n========== YOUR BOOKINGS ==========")
    for i, b in enumerate(booking, start=1):
        print(f"{i}. {b['name']} - RM{b['total']:.2f} total")

    choice = int(input("\nEnter the number of the booking to cancel: "))

    if choice < 1 or choice > len(booking):
        print("\nInvalid choice.")
        return
    
    selected = booking[choice - 1]

    confirm = input(f"Are you sure you want to cancel '{selected['name']}'? (Y/N): ").upper()

    if confirm == "Y":
        booking.pop(choice - 1)
        print(f"\nBooking for {selected['name']} has been cancelled.")
    else:
        print("\nCancellation aborted.")
        

    
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


