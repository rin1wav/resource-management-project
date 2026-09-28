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
    print(f"{title:^60}")
    print("=" * 60)


# ============================================================
# ROOM FUNCTIONS
# ============================================================

def view_rooms():
    print_header("VIEW ROOMS")

    try:
        cursor.execute("SELECT * FROM rooms")
        rooms = cursor.fetchall()

        if not rooms:
            print("No rooms found.")
        else:
            print(
                f"{'ID':<10}"
                f"{'Room No.':<12}"
                f"{'Type':<22}"
                f"{'Price':<10}"
                f"{'Status':<20}"
            )

            print("-" * 74)

            for room in rooms:
                print(
                    f"{room[0]:<10}"
                    f"{room[1]:<12}"
                    f"{room[2]:<22}"
                    f"{room[3]:<10}"
                    f"{room[4]:<20}"
                )

    except Error as e:
        print("Error:", e)

    pause()


def add_room():
    print_header("ADD ROOM")

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
        print("\nPlease enter valid numeric values for ID, room number and price.")

    except Error as e:
        db.rollback()
        print("\nError:", e)

    pause()


def search_room():
    print_header("SEARCH ROOM")

    try:
        room_id = int(input("Enter room ID to search: "))

        query = """
        SELECT * FROM rooms
        WHERE room_id = %s
        """

        cursor.execute(query, (room_id,))
        room = cursor.fetchone()

        if room:
            print("\nRoom found!")
            print("Room ID:", room[0])
            print("Room Number:", room[1])
            print("Room Type:", room[2])
            print("Price:", room[3])
            print("Status:", room[4])
        else:
            print("\nRoom not found.")

    except ValueError:
        print("Please enter a valid room ID.")

    except Error as e:
        print("Error:", e)

    pause()


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

        values = (new_status, room_id)

        cursor.execute(query, values)

        if cursor.rowcount == 0:
            print("\nRoom not found.")
        else:
            db.commit()
            print("\nRoom status updated successfully!")

    except ValueError:
        print("Please enter a valid room ID.")

    except Error as e:
        db.rollback()
        print("Error:", e)

    pause()


# ============================================================
# RESOURCE FUNCTIONS
# ============================================================

def view_resources():
    print_header("VIEW RESOURCES")

    try:
        cursor.execute("SELECT * FROM resources")
        resources = cursor.fetchall()

        if not resources:
            print("No resources found.")
        else:
            print(
                f"{'ID':<10}"
                f"{'Resource':<22}"
                f"{'Category':<18}"
                f"{'Quantity':<12}"
                f"{'Available':<12}"
            )

            print("-" * 74)

            for resource in resources:
                print(
                    f"{resource[0]:<10}"
                    f"{resource[1]:<22}"
                    f"{resource[2]:<18}"
                    f"{resource[3]:<12}"
                    f"{resource[4]:<12}"
                )

    except Error as e:
        print("Error:", e)

    pause()


def add_resource():
    print_header("ADD RESOURCE")

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
        print("\nPlease enter valid numbers for ID and quantities.")

    except Error as e:
        db.rollback()
        print("\nError:", e)

    pause()


# ============================================================
# GUEST FUNCTIONS
# ============================================================

def view_guests():
    print_header("VIEW GUESTS")

    try:
        cursor.execute("SELECT * FROM guests")
        guests = cursor.fetchall()

        if not guests:
            print("No guests found.")
        else:
            print(
                f"{'ID':<10}"
                f"{'Name':<30}"
                f"{'Phone':<15}"
            )

            print("-" * 55)

            for guest in guests:
                print(
                    f"{guest[0]:<10}"
                    f"{guest[1]:<30}"
                    f"{guest[2]:<15}"
                )

    except Error as e:
        print("Error:", e)

    pause()
    # Collects guest details and inserts a new guest record into the guests table
def add_guest():
    print_header("ADD GUEST")

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
        print("\nError:", e)

    pause()

# ============================================================
# BOOKING FUNCTIONS
# ============================================================

def view_bookings():
    print_header("VIEW BOOKINGS")

    try:
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
        else:
            print(
                f"{'Booking ID':<13}"
                f"{'Guest Name':<25}"
                f"{'Room ID':<12}"
                f"{'Date':<15}"
                f"{'Status':<15}"
            )

            print("-" * 80)

            for booking in bookings:
                print(
                    f"{booking[0]:<13}"
                    f"{booking[1]:<25}"
                    f"{booking[2]:<12}"
                    f"{booking[3]:<15}"
                    f"{booking[4]:<15}"
                )

    except Error as e:
        print("Error:", e)

    pause()


def add_booking():
    print_header("CREATE BOOKING")

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
        print("\nPlease enter valid numeric values.")

    except Error as e:
        db.rollback()
        print("\nError:", e)

    pause()


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    while True:

        print_header("HOTEL RESOURCE MANAGEMENT SYSTEM")

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

        elif choice == "2":
            add_room()

        elif choice == "3":
            search_room()

        elif choice == "4":
            update_room()

        elif choice == "5":
            view_resources()

        elif choice == "6":
            add_resource()

        elif choice == "7":
            view_guests()

        elif choice == "8":
            add_guest()

        elif choice == "9":
            view_bookings()

        elif choice == "10":
            add_booking()

        elif choice == "11":
            print("\nThank you for using the Hotel Resource Management System!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 11.")

            pause()


# ============================================================
# PROGRAM START
# ============================================================

try:
    main_menu()

finally:
    cursor.close()
    db.close()

    print("\nDatabase connection closed.")
