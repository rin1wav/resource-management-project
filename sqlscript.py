import mysql.connector
from mysql.connector import Error


# ============================================================
# DATABASE CONNECTION
# ============================================================

try:
    db = mysql.connector.connect(
        host="localhost",
        user="hoteluser",
        password="HotelPass123!",
        database="hotel"
    )

    cursor = db.cursor()

    print("\n" + "=" * 60)
    print("       HOTEL RESOURCE MANAGEMENT SYSTEM")
    print("=" * 60)
    print("Database connected successfully!")

except Error as e:
    print("Database connection failed.")
    print("Error:", e)
    exit()


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def pause():
    input("\nPress Enter to continue...")


def print_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


# ============================================================
# ROOM FUNCTIONS
# ============================================================

def view_rooms():

    print_header("ROOM DETAILS")

    cursor.execute("SELECT * FROM rooms")

    rooms = cursor.fetchall()

    if not rooms:
        print("No rooms found.")
        return

    print(
        f"{'ID':<8}"
        f"{'NUMBER':<12}"
        f"{'TYPE':<22}"
        f"{'PRICE':<10}"
        f"{'STATUS':<18}"
    )

    print("-" * 70)

    for room in rooms:
        print(
            f"{room[0]:<8}"
            f"{room[1]:<12}"
            f"{room[2]:<22}"
            f"{room[3]:<10}"
            f"{room[4]:<18}"
        )


def add_room():

    print_header("ADD NEW ROOM")

    try:
        room_id = int(input("Enter room ID: "))
        room_number = int(input("Enter room number: "))
        room_type = input("Enter room type: ")
        price = int(input("Enter room price: "))
        status = input("Enter room status: ")

        query = """
        INSERT INTO rooms
        (room_id, room_number, room_type, price, status)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            room_id,
            room_number,
            room_type,
            price,
            status
        )

        cursor.execute(query, values)
        db.commit()

        print("\nRoom added successfully!")

    except ValueError:
        print("\nPlease enter valid numerical values.")

    except Error as e:
        db.rollback()
        print("\nCould not add room.")
        print("Error:", e)


def search_room():

    print_header("SEARCH ROOM")

    try:
        room_id = int(input("Enter room ID: "))

        query = """
        SELECT * FROM rooms
        WHERE room_id = %s
        """

        cursor.execute(query, (room_id,))

        room = cursor.fetchone()

        if room:
            print("\nRoom found!")
            print("Room ID     :", room[0])
            print("Room Number :", room[1])
            print("Room Type   :", room[2])
            print("Price       :", room[3])
            print("Status      :", room[4])

        else:
            print("\nRoom not found.")

    except ValueError:
        print("\nPlease enter a valid room ID.")

    except Error as e:
        print("\nError:", e)


def update_room():

    print_header("UPDATE ROOM STATUS")

    try:
        room_id = int(input("Enter room ID: "))
        new_status = input("Enter new status: ")

        query = """
        UPDATE rooms
        SET status = %s
        WHERE room_id = %s
        """

        cursor.execute(query, (new_status, room_id))

        if cursor.rowcount == 0:
            print("\nRoom not found.")
        else:
            db.commit()
            print("\nRoom status updated successfully!")

    except ValueError:
        print("\nPlease enter a valid room ID.")

    except Error as e:
        db.rollback()
        print("\nError:", e)


# ============================================================
# RESOURCE FUNCTIONS
# ============================================================

def view_resources():

    print_header("RESOURCE DETAILS")

    cursor.execute("SELECT * FROM resources")

    resources = cursor.fetchall()

    if not resources:
        print("No resources found.")
        return

    print(
        f"{'ID':<8}"
        f"{'RESOURCE':<22}"
        f"{'CATEGORY':<18}"
        f"{'QUANTITY':<12}"
        f"{'AVAILABLE':<12}"
    )

    print("-" * 72)

    for resource in resources:
        print(
            f"{resource[0]:<8}"
            f"{resource[1]:<22}"
            f"{resource[2]:<18}"
            f"{resource[3]:<12}"
            f"{resource[4]:<12}"
        )


def add_resource():

    print_header("ADD NEW RESOURCE")

    try:
        resource_id = int(input("Enter resource ID: "))
        resource_name = input("Enter resource name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))
        available = int(input("Enter available quantity: "))

        query = """
        INSERT INTO resources
        (resource_id, resource_name, category, quantity, available)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            resource_id,
            resource_name,
            category,
            quantity,
            available
        )

        cursor.execute(query, values)
        db.commit()

        print("\nResource added successfully!")

    except ValueError:
        print("\nPlease enter valid numerical values.")

    except Error as e:
        db.rollback()
        print("\nCould not add resource.")
        print("Error:", e)


# ============================================================
# GUEST FUNCTIONS
# ============================================================

def view_guests():

    print_header("GUEST DETAILS")

    cursor.execute("SELECT * FROM guests")

    guests = cursor.fetchall()

    if not guests:
        print("No guests found.")
        return

    print(
        f"{'ID':<8}"
        f"{'NAME':<22}"
        f"{'PHONE':<16}"
        f"{'CHECK-IN':<15}"
        f"{'CHECK-OUT':<15}"
    )

    print("-" * 76)

    for guest in guests:
        print(
            f"{guest[0]:<8}"
            f"{guest[1]:<22}"
            f"{guest[2]:<16}"
            f"{str(guest[3]):<15}"
            f"{str(guest[4]):<15}"
        )


def add_guest():

    print_header("ADD NEW GUEST")

    try:
        guest_id = int(input("Enter guest ID: "))
        guest_name = input("Enter guest name: ")
        phone = input("Enter phone number: ")
        check_in = input("Enter check-in date (YYYY-MM-DD): ")
        check_out = input("Enter check-out date (YYYY-MM-DD): ")

        query = """
        INSERT INTO guests
        (guest_id, guest_name, phone, check_in, check_out)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            guest_id,
            guest_name,
            phone,
            check_in,
            check_out
        )

        cursor.execute(query, values)
        db.commit()

        print("\nGuest added successfully!")

    except ValueError:
        print("\nPlease enter a valid guest ID.")

    except Error as e:
        db.rollback()
        print("\nCould not add guest.")
        print("Error:", e)


# ============================================================
# BOOKING FUNCTIONS
# ============================================================

def view_bookings():

    print_header("BOOKING DETAILS")

    query = """
    SELECT
        bookings.booking_id,
        guests.guest_name,
        bookings.room_id,
        bookings.booking_date,
        bookings.status
    FROM bookings
    LEFT JOIN guests
        ON bookings.guest_id = guests.guest_id
    """

    cursor.execute(query)

    bookings = cursor.fetchall()

    if not bookings:
        print("No bookings found.")
        return

    print(
        f"{'ID':<8}"
        f"{'GUEST':<22}"
        f"{'ROOM ID':<12}"
        f"{'DATE':<15}"
        f"{'STATUS':<15}"
    )

    print("-" * 72)

    for booking in bookings:
        print(
            f"{booking[0]:<8}"
            f"{booking[1]:<22}"
            f"{booking[2]:<12}"
            f"{str(booking[3]):<15}"
            f"{booking[4]:<15}"
        )


def add_booking():

    print_header("CREATE NEW BOOKING")

    try:
        booking_id = int(input("Enter booking ID: "))
        guest_id = int(input("Enter guest ID: "))
        room_id = int(input("Enter room ID: "))
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        status = input("Enter booking status: ")

        query = """
        INSERT INTO bookings
        (booking_id, guest_id, room_id, booking_date, status)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            booking_id,
            guest_id,
            room_id,
            booking_date,
            status
        )

        cursor.execute(query, values)
        db.commit()

        print("\nBooking created successfully!")

    except ValueError:
        print("\nPlease enter valid numerical values.")

    except Error as e:
        db.rollback()
        print("\nCould not create booking.")
        print("Error:", e)


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        print_header("MAIN MENU")

        print("1. View Rooms")
        print("2. Add Room")
        print("3. Search Room")
        print("4. Update Room Status")
        print("5. View Resources")
        print("6. Add Resource")
        print("7. View Guests")
        print("8. Add Guest")
        print("9. View Bookings")
        print("10. Create Booking")
        print("11. Exit")

        print("-" * 60)

        choice = input("Enter your choice: ")

        if choice == "1":
            view_rooms()
            pause()

        elif choice == "2":
            add_room()
            pause()

        elif choice == "3":
            search_room()
            pause()

        elif choice == "4":
            update_room()
            pause()

        elif choice == "5":
            view_resources()
            pause()

        elif choice == "6":
            add_resource()
            pause()

        elif choice == "7":
            view_guests()
            pause()

        elif choice == "8":
            add_guest()
            pause()

        elif choice == "9":
            view_bookings()
            pause()

        elif choice == "10":
            add_booking()
            pause()

        elif choice == "11":
            print("\nThank you for using the Hotel Resource Management System.")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")


# ============================================================
# START PROGRAM
# ============================================================

main_menu()

cursor.close()
db.close()

print("Database connection closed.")