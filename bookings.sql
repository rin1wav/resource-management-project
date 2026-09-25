CREATE TABLE bookings (
    booking_id INT PRIMARY KEY NOT NULL,
    guest_id INT NOT NULL,
    room_id INT NOT NULL,
    booking_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);
INSERT INTO bookings
VALUES
(1, 1, 1, '2026-09-20', 'Completed'),
(2, 2, 2, '2026-09-21', 'Active'),
(3, 3, 3, '2026-09-22', 'Active'),
(4, 4, 4, '2026-09-23', 'Cancelled'),
(5, 5, 5, '2026-09-24', 'Active');
