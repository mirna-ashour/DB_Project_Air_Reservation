INSERT INTO Airline VALUES (‘Jet Blue’);

INSERT INTO Airport(Name, City, Country, Type) VALUES ('JFK', 'New York City', 'US', 'Int'),
	('PVG', 'Shanghai', 'China', 'Int');

INSERT INTO Customer VALUES ('mirna@nyu.edu', 'password123', 'Mirna', 
'Ashour', 152, 'Montague', 3, 'Brooklyn', 'New York', 11201, '1431243', 
'2025-01-01', 'US', '2002-11-20'),

('olivia@nyu.edu', 'password123', 'Olivia', 'Marcelin', 100, 'Orange', 4, 'Brooklyn', 'New York', 11201, '385647', '2028-04-01', 'US', '2002-05-10'),

(‘nisha@nyu.edu', 'password123', 'Nisha', 'Ramanna', 11, 'Hoyt', 39, 'Brooklyn', 'New York', 11201, '2454513', '2026-04-08', 'US', '2002-09-02');

INSERT INTO Airplane VALUES ('Jet Blue', 1, 200, 'BOEING', '2020-05-11', 12),
 ('Jet Blue', 1, 300, 'BOEING', '2006-04-01', 20),  ('Jet Blue', 1, 50, 'BOEING', '2022-08-10', 30);

INSERT INTO airline_staff VALUES ('marthastew123', 'Jet Blue', 
, 'Martha1234', 'Martha', 'Stewart', '1972-11-05');
	
INSERT INTO staff_phone_num VALUES ('marthastew123', 1234567');

INSERT INTO staff_email VALUES ('marthastew123',
'marthas@gmail.com');

INSERT INTO Flight VALUES ('Jet Blue', 3456, '18:19:03', '2023-08-05',  '23:19:03', '2023-08-05', 1, 2, 400, 'on-time'),
                           
('Jet Blue', 3894, '12:04:19', '2023-04-19',  '18:03:03', '2023-08-06', 2, 1, 1000, 'on-time'),
                           
('Jet Blue', 9353, '03:19:03', '2023-03-22',  '16:08:18', '2023-03-22', 1, 2, 297, 'delayed');

INSERT INTO Ticket() VALUES
('Jet Blue', 3456, ‘18:19:03', '2023-08-05’,  'Mirna', 'Ashour', ‘2002-11-20’, 2746728, 'Mirna Ashour', ’2023-05-05’, ‘2002-06-12’, ‘02:06:12, 'debit'),

('Jet Blue', 3894, ‘12:04:19', '2023-04-19’,  ‘Olivia’, Marcelin, ‘2002-06-12’, 3984275, 'Olivia Marcelin', ‘2010-02-22, ‘2023-08-06’, 10:20:22, 'credit'),

('Jet Blue', 3894, ‘12:04:19', '2023-04-19’, ‘Jeff’, ‘Bezos’, ‘1987-04-80’, 398425, 'Olivia Marcelin', ‘2010-02-22’, ‘2023-08-06’,10:20:22, 'debit'),

('Jet Blue', 9353, ‘03:19:03', '2023-03-22’, 'Nisha', 'Ramanna', ‘2002-10-20’, 2453489, 'Nisha Ramanna',  ‘2023-03-22’’, ‘2021-06-04’ , 21:16:04, 'debit');


INSERT INTO Ticket(Airline_name, Flight_num, Departure_time, Departure_date, FirstName, LastName, Date_of_birth, Card_num, Name_on_card, Expiration_date, Purchase_date, Purchase_time, Card_type) VALUES
('Jet Blue', 3456, ‘18:19:03', '2023-08-05’,  'Mirna', 'Ashour', ‘2002-11-20’, 2746728, 'Mirna Ashour', ’2023-05-05’, ‘2002-06-12’, ‘02:06:12, 'debit'),

('Jet Blue', 3894, ‘12:04:19', '2023-04-19’,  ‘Olivia’, Marcelin, ‘2002-06-12’, 3984275, 'Olivia Marcelin', ‘2010-02-22, ‘2023-08-06’, 10:20:22, 'credit'),

('Jet Blue', 3894, ‘12:04:19', '2023-04-19’, ‘Jeff’, ‘Bezos’, ‘1987-04-80’, 398425, 'Olivia Marcelin', ‘2010-02-22’, ‘2023-08-06’,10:20:22, 'debit'),

('Jet Blue', 9353, ‘03:19:03', '2023-03-22’, 'Nisha', 'Ramanna', ‘2002-10-20’, 2453489, 'Nisha Ramanna',  ‘2023-03-22’’, ‘2021-06-04’ , 21:16:04, 'debit'),






