# 🏨 Resource Management Project

A simple **Resource Management System** based on the working of a hotel, developed as a school project using **Python and MySQL**.

## 📌 About the Project

This project demonstrates how a relational database can be used to manage and organize resources in a hotel.

The system keeps track of:

* 🛏️ Hotel rooms
* 📦 Hotel resources
* 👤 Guests
* 📋 Room bookings

The project uses **MySQL** to store and manage the data, while **Python** is used to interact with the database and provide the user interface.

## 🛠️ Technologies Used

* **Python** — Application logic and user interaction
* **MySQL** — Database management
* **SQL** — Creating, storing, retrieving, and modifying data

## 🗄️ Database Structure

The database contains four main tables:

### `rooms`

Stores information about hotel rooms.

| Field         | Description           |
| ------------- | --------------------- |
| `room_id`     | Unique ID of the room |
| `room_number` | Hotel room number     |
| `room_type`   | Type of room          |
| `price`       | Price per night       |
| `status`      | Current room status   |

### `resources`

Stores information about resources available in the hotel.

| Field           | Description                  |
| --------------- | ---------------------------- |
| `resource_id`   | Unique resource ID           |
| `resource_name` | Name of the resource         |
| `category`      | Resource category            |
| `quantity`      | Total quantity               |
| `available`     | Currently available quantity |

### `guests`

Stores information about hotel guests.

| Field        | Description       |
| ------------ | ----------------- |
| `guest_id`   | Unique guest ID   |
| `guest_name` | Name of the guest |
| `phone`      | Contact number    |
| `check_in`   | Check-in date     |
| `check_out`  | Check-out date    |

### `bookings`

Stores information about room bookings.

| Field          | Description           |
| -------------- | --------------------- |
| `booking_id`   | Unique booking ID     |
| `guest_id`     | ID of the guest       |
| `room_id`      | ID of the booked room |
| `booking_date` | Date of booking       |
| `status`       | Booking status        |

## 💻 SQL Features Demonstrated

The project demonstrates several fundamental SQL operations, including:

* `CREATE DATABASE`
* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `WHERE`
* `UPDATE`
