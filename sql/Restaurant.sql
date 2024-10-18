CREATE TABLE Restaurant (
    Name NVARCHAR(100),
    Address NVARCHAR(255),
    Style NVARCHAR(50),
    Vegetarian BIT,
    DoesDeliveries BIT,
    OpeningHour TIME,
    ClosingHour TIME
);

INSERT INTO Restaurant (Name, Address, Style, Vegetarian, DoesDeliveries, OpeningHour, ClosingHour)
VALUES 
('Pizza Hut', 'Ben Hillel 15, Jerusalem', 'Italian', 1, 1, '09:00', '21:00'),
('Nini Hachi', 'Ben Yehuda 228, Tel Aviv', 'Japanese', 0, 1, '11:00', '23:00'),
('Sogo', 'Gaaton Jabotinski 1, Nahariya', 'Steakhouse', 0, 0, '10:00', '22:00'),
('Rak Dagim', 'Tarshish 7, Eilat', 'Seafood', 0, 0, '09:00', '21:00');
