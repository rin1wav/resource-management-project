CREATE TABLE guests (
    guest_id INT PRIMARY KEY NOT NULL,
    guest_name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL
);
INSERT INTO guests
VALUES
(1, 'Arjun Kumar', '9876543210', '2026-09-20', '2026-09-23'),
(2, 'Meera Nair', '9876543211', '2026-09-21', '2026-09-25'),
(3, 'Rahul Menon', '9876543212', '2026-09-22', '2026-09-27'),
(4, 'Ananya Das', '9876543213', '2026-09-23', '2026-09-26'),
(5, 'Vivek Sharma', '9876543214', '2026-09-24', '2026-09-28');
