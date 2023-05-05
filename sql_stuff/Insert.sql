INSERT INTO Airline VALUES ('Jet Blue');

INSERT INTO Airport(Name, City, Country, Type) VALUES ('JFK', 'New York City', 'US', 'Int'),
	('PVG', 'Shanghai', 'China', 'Int'), ('BNA', 'Nashville', 'TN', 'Dom');

INSERT INTO Customer VALUES ('mirna@nyu.edu', 'password123', 'Mirna', 
'Ashour', 152, 'Montague', 3, 'Brooklyn', 'New York', 11201, '1431243', 
'2025-01-01', 'US', '2002-11-20'),

('olivia@nyu.edu', 'password123', 'Olivia', 'Marcelin', 100, 'Orange', 4, 'Brooklyn', 'New York', 11201, '385647', '2028-04-01', 'US', '2002-05-10'),

('nisha@nyu.edu', 'password123', 'Nisha', 'Ramanna', 11, 'Hoyt', 39, 'Brooklyn', 'New York', 11201, '2454513', '2026-04-08', 'US', '2002-09-02');

INSERT INTO Airplane(Airline_name, Num_of_seats, Manufacturing_company, Manufacturing_date, Age) VALUES ('Jet Blue', 200, 'BOEING', '2020-05-11', 2),
 ('Jet Blue', 300, 'BOEING', '2006-04-01', 17),  ('Jet Blue', 50, 'BOEING', '2022-08-10', 0);

INSERT INTO airline_staff VALUES ('marthastew123', 'Jet Blue', 'Martha1234', 'Martha', 'Stewart', '1972-11-05');
	
INSERT INTO staff_phone_num VALUES ('marthastew123', '1234567');

INSERT INTO staff_email VALUES ('marthastew123',
'marthas@gmail.com');

INSERT INTO Flight VALUES ('Jet Blue', 3456, '18:19:03', '2023-08-05',  '23:19:03', '2023-08-05', 1, 2, 400, 3, 'on-time'),
                           
('Jet Blue', 3894, '12:04:19', '2023-04-19',  '18:03:03', '2023-08-06', 2, 1, 1000, 1, 'on-time'),
                           
('Jet Blue', 9353, '03:19:03', '2023-03-22',  '16:08:18', '2023-03-22', 1, 2, 297, 2, 'delayed'),

('Jet Blue', 10204, '05:27:35', '2023-05-17',  '08:56:18', '2023-05-17', 1, 3, 158, 3, 'on-time'),

('Jet Blue', 58748, '05:27:35', '2023-05-05',  '08:56:18', '2023-05-05', 1, 3, 158, 2, 'on-time'),

('Jet Blue', 9238, '15:19:03', '2023-05-06',  '17:19:03', '2023-05-06', 1, 2, 400, 3, 'on-time'),

('Jet Blue', 9238, '15:19:03', '2023-07-04', '17:19:03', '2023-07-04', 1, 2, 400, 3, 'on-time'),

('Jet Blue', 1298, '05:35:35', '2021-04-17', '06:56:12', '2021-04-17', 2, 3, 390, 1, 'delayer');

INSERT INTO Ticket(Email, Airline_name, Flight_num, Departure_time, Departure_date, FirstName, LastName, Date_of_birth, Card_num, Name_on_card, Expiration_date,
Purchase_date, Purchase_time, Card_type) VALUES
('mirna@nyu.edu', 'Jet Blue', 3456, '18:19:03', '2023-08-05',  'Mirna', 'Ashour', '2002-11-20', 2746728, 'Mirna Ashour', '2023-05-05', '2002-06-12', '02:06:12', 'debit'),

('olivia@nyu.edu', 'Jet Blue', 3894, '12:04:19', '2023-04-19',  'Olivia', 'Marcelin', '2002-06-12', 3984275, 'Olivia Marcelin', '2010-02-22', '2023-08-06', '10:20:22', 'credit'),

('olivia@nyu.edu', 'Jet Blue', 3894, '12:04:19', '2023-04-19', 'Jeff', 'Bezos', '1987-04-08', 398425, 'Olivia Marcelin', '2010-02-22', '2023-08-06', '10:20:22', 'debit'),

('nisha@nyu.edu', 'Jet Blue', 9353, '03:19:03', '2023-03-22', 'Nisha', 'Ramanna', '2002-10-20', 2453489, 'Nisha Ramanna',  '2023-03-22', '2021-06-04', '21:16:04', 'debit'),

('nisha@nyu.edu', 'Jet Blue', 58748, '05:27:35', '2023-05-05', 'Nisha', 'Ramanna', '2002-10-20', 2453489, 'Nisha Ramanna',  '2023-03-22', '2021-06-04', '21:16:04', 'debit'),

('nisha@nyu.edu', 'Jet Blue', 1298, '05:35:35', '2021-04-17', 'Nisha', 'Ramanna', '2002-10-20', 2453489, 'Nisha Ramanna',  '2021-02-15', '2021-06-04', '21:16:04', 'debit'),

('nisha@nyu.edu', 'Jet Blue', 9238, '15:19:03', '2023-05-06', 'Nisha', 'Ramanna', '2002-10-20', 2453489, 'Nisha Ramanna',  '2021-02-15', '2021-06-04', '21:16:04', 'debit'),

('nisha@nyu.edu', 'Jet Blue', 9238, '15:19:03', '2023-07-04', 'Nisha', 'Ramanna', '2002-10-20', 2453489, 'Nisha Ramanna',  '2021-02-15', '2021-06-04', '21:16:04', 'debit');