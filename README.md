# 🏨 Hotel Resource Management System

A **Hotel Resource Management System** developed using **Python and MySQL**.

This project is designed to manage important hotel information such as rooms, guests, hotel resources, and bookings. Python is used for the application logic and user interface, while MySQL is used to store and manage the data.

---

## 📌 About the Project

The Hotel Resource Management System is a menu-driven Python application connected to a MySQL database.

The system allows the user to:

- View hotel rooms
- Add new rooms
- Search for rooms
- Update room status
- View hotel resources
- Add new resources
- View guest information
- Add new guests
- View bookings
- Create new bookings
- Store information permanently in a MySQL database

The main purpose of this project is to demonstrate how **Python can interact with a relational database using MySQL**.

---

## 🛠️ Technologies Used

### Python

Python is used for:

- Application logic
- Menu creation
- Taking input from the user
- Displaying database records
- Sending SQL queries to MySQL
- Inserting and updating records
- Handling errors

### MySQL

MySQL is used as the database management system.

It stores information about:

- Rooms
- Resources
- Guests
- Bookings

### MySQL Connector for Python

The Python program communicates with MySQL using the `mysql-connector-python` package.

The connector allows Python to:

- Connect to the MySQL server
- Execute SQL queries
- Retrieve database records
- Insert new records
- Update existing records
- Handle database errors

---

# 📂 Database Structure

The project uses a database named:

```text
hotel
```

The database contains four main tables.

## 1. Rooms

The `rooms` table stores information about hotel rooms.

| Column | Data Type | Description |
|---|---|---|
| room_id | INT | Unique ID of the room |
| room_number | INT | Room number |
| room_type | VARCHAR(30) | Type of room |
| price | INT | Room price |
| status | VARCHAR(20) | Current room status |

Example room types include:

- SINGLE-SUITE
- DOUBLE-SUITE
- LUXURY-SUITE
- BUSINESS-SUITE
- FAMILY-DELUXE

---

## 2. Resources

The `resources` table stores hotel resources and their quantities.

| Column | Data Type | Description |
|---|---|---|
| resource_id | INT | Unique resource ID |
| resource_name | VARCHAR(20) | Name of the resource |
| category | VARCHAR(20) | Resource category |
| quantity | INT | Total quantity |
| available | INT | Currently available quantity |

Examples of resources include:

- Bath Towels
- Bed Sheets
- Shampoo
- Soap
- Cleaning Mops

---

## 3. Guests

The `guests` table stores information about hotel guests.

| Column | Data Type | Description |
|---|---|---|
| guest_id | INT | Unique guest ID |
| guest_name | VARCHAR(50) | Guest name |
| phone | VARCHAR(15) | Contact number |
| check_in | DATE | Check-in date |
| check_out | DATE | Check-out date |

---

## 4. Bookings

The `bookings` table stores information about room bookings.

| Column | Data Type | Description |
|---|---|---|
| booking_id | INT | Unique booking ID |
| guest_id | INT | ID of the guest |
| room_id | INT | ID of the booked room |
| booking_date | DATE | Date of booking |
| status | VARCHAR(20) | Booking status |

The bookings table connects guests with rooms.

---

# 🔗 Python + MySQL Integration

Python communicates with MySQL using the `mysql.connector` module.

The basic system works like this:

```text
Python Program
      ↓
mysql.connector
      ↓
MySQL Server
      ↓
hotel Database
      ↓
Tables
```

The Python program sends SQL commands to MySQL and receives the results.

For example:

```python
cursor.execute("SELECT * FROM rooms")
rooms = cursor.fetchall()
```

The SQL query retrieves all records from the `rooms` table, and Python then displays the records to the user.

---

# 💻 Installation

## 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installed version:

```bash
python3 --version
```

A Python version should be displayed.

Example:

```text
Python 3.x.x
```

---

## 2. Install MySQL

Install MySQL Server on your system.

Check whether MySQL is installed:

```bash
mysql --version
```

A MySQL version should be displayed.

---

## 3. Create the Database

Open the MySQL command line:

```bash
mysql -u root -p
```

Create the project database:

```sql
CREATE DATABASE hotel;
```

Select the database:

```sql
USE hotel;
```

The SQL file included in this repository can then be used to create the required tables and insert sample data.

---

# 🐍 Installing MySQL Connector for Python

The Python program requires the `mysql-connector-python` package.

Install it using:

```bash
python3 -m pip install mysql-connector-python
```

If you are using a Python virtual environment, activate the environment first:

```bash
source hotelenv/bin/activate
```

Then install the connector:

```bash
python -m pip install mysql-connector-python
```

To verify that the connector was installed successfully:

```bash
python -c "import mysql.connector; print('MYSQL CONNECTOR WORKS')"
```

If everything is installed correctly, the following message should appear:

```text
MYSQL CONNECTOR WORKS
```

---

# 🔐 MySQL User Configuration

A separate MySQL user can be created for the application.

Example:

```sql
CREATE USER 'hoteluser'@'localhost'
IDENTIFIED BY 'YOUR_PASSWORD';

GRANT ALL PRIVILEGES ON hotel.*
TO 'hoteluser'@'localhost';

FLUSH PRIVILEGES;
```

Replace `YOUR_PASSWORD` with your own password.

> **Important:** Never upload your real MySQL password to GitHub.

---

# ⚙️ Configuring the Python Program

The Python program connects to MySQL using:

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="hoteluser",
    password="YOUR_PASSWORD",
    database="hotel"
)
```

Change `YOUR_PASSWORD` to the password of your MySQL user.

The database name should be:

```text
hotel
```

---

# ▶️ Running the Program

Clone the repository:

```bash
git clone https://github.com/rin1wav/resource-management-project.git
```

Move into the project directory:

```bash
cd resource-management-project
```

If you are using a virtual environment:

```bash
source hotelenv/bin/activate
```

Install the required Python package:

```bash
python -m pip install mysql-connector-python
```

Run the Python program:

```bash
python hotel_management.py
```

If the Python file is located inside a `python` folder, use:

```bash
python python/hotel_management.py
```

---

# 📋 Main Menu

The application provides a menu similar to:

```text
============================================================
       HOTEL RESOURCE MANAGEMENT SYSTEM
============================================================

1. View Rooms
2. Add Room
3. Search Room
4. Update Room Status
5. View Resources
6. Add Resource
7. View Guests
8. Add Guest
9. View Bookings
10. Create Booking
11. Exit
```

The user can select an option by entering the corresponding number.

---

# 🗃️ Features

## View Rooms

Displays all rooms stored in the MySQL database.

The information displayed includes:

- Room ID
- Room number
- Room type
- Price
- Status

---

## Add Room

Allows the user to enter information for a new room.

The user provides:

- Room ID
- Room number
- Room type
- Price
- Room status

The information is then inserted into the MySQL database.

---

## Search Room

The user can search for a room using its room ID.

The Python program sends a parameterized SQL query to MySQL:

```python
cursor.execute(
    "SELECT * FROM rooms WHERE room_id = %s",
    (room_id,)
)
```

This allows the program to safely use user-provided values in SQL queries.

---

## Update Room Status

The application can update the status of a room.

For example:

```text
OCCUPIED
NOT OCCUPIED
```

The Python program sends an `UPDATE` query to MySQL.

After modifying the database, the program uses:

```python
db.commit()
```

to save the changes.

---

## View Resources

Displays resources stored in the hotel database.

Examples include:

```text
Bath Towels
Bed Sheets
Shampoo
Soap
Cleaning Mops
```

The system displays their total and available quantities.

---

## Add Resource

Allows a new hotel resource to be added to the database.

The user enters:

- Resource ID
- Resource name
- Category
- Quantity
- Available quantity

The information is then inserted into MySQL.

---

## View Guests

Displays guest information stored in the database.

This includes:

- Guest ID
- Guest name
- Phone number
- Check-in date
- Check-out date

---

## Add Guest

Allows the user to register a new guest.

The entered information is stored permanently in the MySQL database.

---

## View Bookings

Displays existing bookings.

The program uses an SQL `JOIN` to obtain the guest name from the `guests` table.

Example:

```sql
SELECT
    bookings.booking_id,
    guests.guest_name,
    bookings.room_id,
    bookings.booking_date,
    bookings.status
FROM bookings
LEFT JOIN guests
    ON bookings.guest_id = guests.guest_id;
```

This demonstrates how related tables can be combined using SQL.

---

## Create Booking

The user can create a new booking by entering:

- Booking ID
- Guest ID
- Room ID
- Booking date
- Booking status

The information is then inserted into the `bookings` table.

---

# 🧠 Python Concepts Used

The project demonstrates several Python concepts:

- Variables
- Input and output
- Conditional statements
- Loops
- Functions
- Tuples
- Exception handling
- SQL queries
- Database connectivity
- User-defined functions
- Menu-driven programming

---

# 🗄️ SQL Concepts Used

The project demonstrates several MySQL concepts:

- `CREATE DATABASE`
- `CREATE TABLE`
- `INSERT`
- `SELECT`
- `UPDATE`
- `WHERE`
- `JOIN`
- Primary keys
- Data types
- Constraints
- Database relationships

---

# 🔄 CRUD Operations

The project demonstrates the main database operations:

| Operation | SQL Command | Project Example |
|---|---|---|
| Create | INSERT | Add a guest |
| Read | SELECT | View rooms |
| Update | UPDATE | Change room status |
| Delete | DELETE | Future improvement |

The current application mainly implements **Create, Read and Update** operations.

---

# 🛡️ Error Handling

The Python application uses exception handling to handle database errors.

Example:

```python
try:
    # Database operation
except Error as e:
    print("Error:", e)
```

The application can also use:

```python
db.rollback()
```

when an operation fails.

This prevents an unsuccessful database transaction from being saved.

---

# 📁 Project Structure

The repository can be organized as follows:

```text
resource-management-project/
│
├── database/
│   └── hotel_management.sql
│
├── python/
│   └── hotel_management.py
│
├── screenshots/
│   ├── rooms_structure.png
│   ├── rooms_data.png
│   ├── resources_structure.png
│   ├── resources_data.png
│   ├── guests_structure.png
│   ├── guests_data.png
│   ├── bookings_structure.png
│   └── bookings_data.png
│
└── README.md
```

---

# 🔬 System Workflow

The basic working process is:

```text
User
  ↓
Python Menu
  ↓
Python Function
  ↓
SQL Query
  ↓
MySQL Connector
  ↓
MySQL Server
  ↓
Hotel Database
  ↓
Result
  ↓
Python
  ↓
User
```

For example, when the user selects **View Rooms**:

```text
User selects "View Rooms"
          ↓
Python calls view_rooms()
          ↓
Python executes SELECT query
          ↓
MySQL searches the rooms table
          ↓
MySQL returns the records
          ↓
Python receives the records
          ↓
Python displays them
```

---

# 🎯 Objectives

The main objectives of this project are:

1. To develop a simple hotel management application.
2. To understand database management using MySQL.
3. To understand Python-MySQL connectivity.
4. To learn how SQL queries can be executed through Python.
5. To demonstrate storing and retrieving data from a relational database.
6. To understand primary keys and relationships between tables.
7. To implement a menu-driven Python application.
8. To demonstrate basic database operations.

---

# 📚 Educational Purpose

This project was developed as an educational project to demonstrate the integration of **Python programming with MySQL database management**.

It provides practical experience in:

- Python programming
- SQL
- Database design
- Database connectivity
- Data management
- Exception handling

---

# 🚀 Future Improvements

Possible future improvements include:

- Delete records
- Login system
- Admin and staff accounts
- Automatic room availability checking
- Automatic billing
- Invoice generation
- Search by guest name
- Resource usage tracking
- Graphical user interface
- Web-based interface
- Better input validation
- Automatic database backup

---

# 📌 Project Status

The project currently includes:

- MySQL database
- Four database tables
- Sample data
- Python-MySQL connectivity
- Menu-driven Python application
- Room management
- Resource management
- Guest management
- Booking management
- Create, Read and Update operations
- Basic error handling

---

# 👨‍💻 Author

**Kaori**

Class 12 Computer Science Project

**Project:** Hotel Resource Management System

**Technologies:** Python + MySQL
