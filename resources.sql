CREATE TABLE resources (
    resource_id INT PRIMARY KEY NOT NULL,
    resource_name VARCHAR(20) NOT NULL,
    category VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    available VARCHAR(20) NOT NULL
);
INSERT INTO resources
VALUES
(101, 'Bath Towels', 'Linen', 100, '80'),
(102, 'Bed Sheets', 'Linen', 150, '120'),
(103, 'Shampoo', 'Toiletries', 200, '175'),
(104, 'Soap', 'Toiletries', 250, '220'),
(105, 'Cleaning Mops', 'Cleaning', 30, '25');
