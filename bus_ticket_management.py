# packages 
import random
import datetime
import time as t

# Bus data
bus1 = {
    "bus_number": "1101",
    "bus_seats": 30,
    "bus_seat_acq": 15,
    "bus_timing": "10:00 AM",
    "destination": "Banglore",
}

bus2 = {
    "bus_number": "1102",
    "bus_seats": 40,
    "bus_seat_acq": 10,
    "bus_timing": "02:00 PM",
    "destination": "Hospet"
}

buses = [bus1, bus2]
tickets = []

# User data
user = {
    "id": 101,
    "password": "Adex123",
    "user_name": "Adex_111",
    "phone_number": 9916259080,
    "email": "adex11@gmail.com"
}

# Start the program
print("..... (initializing program)", flush=True)
t.sleep(1.5)
print("..... (initializing packages)", flush=True)
t.sleep(1.5)
print("..... (fetching data)", flush=True)
t.sleep(1.5)
print("\n** Welcome to Adex's Bus Services. **\n")

# OTP verification
def verify_otp():
    otp = str(random.randint(1000, 9999))
    print(f"[OTP]: {otp} (Don't share this)")
    for i in range(3):
        entered = input("Enter OTP: ")
        if entered == otp:
            print("OTP verified ✅")
            return
        else:
            print("Incorrect OTP.")
    print("Failed OTP verification. Try again later.")
    exit()

# Authentication
def user_auth(user):
    try:
        ch = int(input("\tLog-in or Sign-up? (0 for Login / 1 for Signup): "))
        if ch == 0:
            chance = 3
            while chance > 0:
                input_username = input("Enter your username: ")
                input_password = input("Enter password: ")
                if input_username != user["user_name"]:
                    print("Invalid Username. Try again.")
                    chance -= 1
                elif input_password != user["password"]:
                    print("Incorrect password. Try again.")
                    chance -= 1
                else:
                    print("Login successful ✅")
                    t.sleep(1)
                    bus_interface(user)
                    return
            print("\n Try another way:")
            chance2 = 3
            while chance2 > 0:
                ch2 = int(input("1) Phone number \n2) Email \nEnter your choice: "))
                if ch2 == 1:
                    input_phone = int(input("Enter your phone number: "))
                    if input_phone == user["phone_number"]:
                        print("Phone number matched!")
                        verify_otp()
                        bus_interface(user)
                        return
                    else:
                        print("Phone number incorrect!")
                        chance2 -= 1
                elif ch2 == 2:
                    input_email = input("Enter your email: ")
                    if input_email == user["email"]:
                        print("Email matched!")
                        verify_otp()
                        bus_interface(user)
                        return
                    else:
                        print("Email not matched!")
                        chance2 -= 1
                else:
                    print("Invalid choice!")
        elif ch == 1:
            print("\n--- SIGN UP ---")
            input_username = input("Enter new username: ")
            input_password = input("Enter new password: ")
            input_phone = int(input("Enter your phone number: "))
            if len(str(input_phone)) != 10:
                print("Invalid phone number.")
                return
            input_email = input("Enter your email: ")
            print("Sending OTP...", flush=True)
            t.sleep(1.5)
            verify_otp()
            user["user_name"] = input_username
            user["password"] = input_password
            user["phone_number"] = input_phone
            user["email"] = input_email
            print("Signup successful ✅")
            t.sleep(1)
            bus_interface(user)
        else:
            print("Invalid option.")
    except ValueError:
        print("Enter only valid numbers where expected.")

# Main menu interface
def bus_interface(user):
    while True:
        print("\n===== Welcome,", user["user_name"], "=====")
        print("\nOur services:")
        print("\t1) Search Bus\n\t2) Book Ticket\n\t3) Cancel Ticket\n\t4) Logout")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            search_bus(user, buses)
        elif ch == 2:
            book_ticket(user, buses, tickets)
        elif ch == 3:
            cancel_ticket(user, buses, tickets)
        elif ch == 4:
            logout()
        else:
            print("Invalid input. Try again.")

# Search Bus
def search_bus(user, buses):
    print("| SEARCHING FOR BUS |")
    chance = 3
    while chance > 0:
        ch = int(input("Search by: 0 = Bus Number, 1 = Destination: "))
        if ch == 0:
            input_query = input("Enter bus number: ")
            for i in buses:
                if i["bus_number"] == input_query:
                    print("Bus found!")
                    bus_found(input_query, user)
                    return
            print("Bus not found.")
            chance -= 1
        elif ch == 1:
            input_query = input("Enter destination: ")
            for i in buses:
                if i["destination"].lower() == input_query.lower():
                    print("Bus found!")
                    bus_found(i["bus_number"], user)
                    return
            print("No buses found for that destination.")
            chance -= 1
        else:
            print("Invalid input.")
            chance -= 1
    else:
        print("Too many failed attempts.")

# Show bus details
def bus_found(input_query, user):
    for bus in buses:
        if bus["bus_number"] == input_query:
            print(f"\n===== Bus Details for {user['user_name']} =====")
            print(f"Bus Number   : {bus['bus_number']}")
            print(f"Total Seats  : {bus['bus_seats']}")
            print(f"Occupied     : {bus['bus_seat_acq']}")
            print(f"Available    : {bus['bus_seats'] - bus['bus_seat_acq']}")
            print(f"Departure    : {bus['bus_timing']}")
            print(f"Destination  : {bus['destination']}")
            return
    print("No matching bus found.")

# Booking Ticket
def book_ticket(user, buses, tickets):
    print("\t | BOOKING TICKETS |")
    ch = int(input("Confirm booking? (yes = 1 / no = 0): "))
    if ch != 1:
        print("Booking cancelled.")
        return

    t.sleep(1.4)
    name = input("Enter passenger name: ")
    number_passenger = int(input("Total passengers: "))
    minor_type = int(input("Minor passengers: "))
    major_type = int(input("Major passengers: "))
    location = input("Boarding location: ")
    destination = input("Enter destination: ")
    bus_select = input("Enter bus number: ")

    for bus in buses:
        if bus["bus_number"] == bus_select and bus["destination"].lower() == destination.lower():
            available_seats = bus["bus_seats"] - bus["bus_seat_acq"]
            if number_passenger > available_seats:
                print(f"Only {available_seats} seats available.")
                return
            bus["bus_seat_acq"] += number_passenger
            ticket_data = {
                "name": name,
                "user": user["user_name"],
                "from": location,
                "to": destination,
                "bus_number": bus["bus_number"],
                "passenger_count": number_passenger,
                "minors": minor_type,
                "majors": major_type,
                "time": bus["bus_timing"]
            }
            tickets.append(ticket_data)
            print("\n=== TICKET CONFIRMED ===")
            print(f"Passenger     : {ticket_data['name']}")
            print(f"From          : {ticket_data['from']}")
            print(f"To            : {ticket_data['to']}")
            print(f"Bus Number    : {ticket_data['bus_number']}")
            print(f"Time          : {ticket_data['time']}")
            print(f"Seats Booked  : {ticket_data['passenger_count']} (Minors: {ticket_data['minors']}, Majors: {ticket_data['majors']})")
            print("Enjoy your journey! 🚍")
            return
    print("No matching bus found.")

# Cancel Ticket
def cancel_ticket(user, buses, tickets):
    print("\t | CANCEL TICKET |")
    if not tickets:
        print("No tickets found.")
        return
    name = input("Enter passenger name: ")
    bus_number = input("Enter bus number: ")

    found = False
    for ticket in tickets:
        if (ticket["name"].lower() == name.lower() and 
            ticket["bus_number"] == bus_number and 
            ticket["user"] == user["user_name"]):
            passenger_count = ticket["passenger_count"]
            for bus in buses:
                if bus["bus_number"] == bus_number:
                    bus["bus_seat_acq"] -= passenger_count
                    break
            tickets.remove(ticket)
            print("\n=== TICKET CANCELLED SUCCESSFULLY ===")
            print(f"Booking for {name} on Bus {bus_number} is cancelled.")
            print(f"{passenger_count} seat(s) released.")
            found = True
            break
    if not found:
        print("Ticket not found.")

# Exit
def logout():
    print("Thank you for using Adex's Bus Services. 🙏")
    exit()

# Entry Point
if __name__ == "__main__":
    user_auth(user)
