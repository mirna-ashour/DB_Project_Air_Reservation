CREATE TABLE Customer (
	Email			varchar(255),
	Password		varchar(255) NOT NULL,
	FirstName		varchar(255) NOT NULL,
	LastName		varchar(255) NOT NULL,
	Building_num		int NOT NULL,
	Street_name		varchar(255) NOT NULL,
	Apartment_num	varchar(255),
	City			varchar(255) NOT NULL,
	State			varchar(255) NOT NULL,
	Zip_code		int NOT NULL,
	Passport_num		int NOT NULL,
	Passport_expiration	date NOT NULL,
	Passport_country	varchar(255) NOT NULL,
	Date_of_birth		date NOT NULL,
	PRIMARY KEY (Email)
);

CREATE TABLE Cust_phone_num(
	Email			varchar(255),
	Phone_num		int NOT NULL,
	PRIMARY KEY (Email)
);

CREATE TABLE Airport (
	Airport_ID		int AUTO_INCREMENT, 
	Name			varchar(255) NOT NULL, 
	City			varchar(255) NOT NULL, 
	Country		varchar(255) NOT NULL, 
	Type			varchar(13) NOT NULL,
	PRIMARY KEY (Airport_ID)
);

CREATE TABLE Airline (
	Name			varchar(255),
	PRIMARY KEY (Name)
);

CREATE TABLE Airplane (
	Airplane_ID		int AUTO_INCREMENT, 
	Airline_name		varchar(255),
	Num_of_seats		int NOT NULL, 
	Manufacturing_company varchar(255) NOT NULL, 
	Manufacturing_date	date NOT NULL, 
	Age			int NOT NULL,
	FOREIGN KEY (Airline_name) REFERENCES Airline(Name),
	PRIMARY KEY (Airplane_ID, Airline_name)
);

CREATE TABLE Airline_Staff (
	Username		varchar(255), 
	Airline_name		varchar(255),
	Password		varchar(255) NOT NULL,
	First_name		varchar(255) NOT NULL, 
	Last_name		varchar(255) NOT NULL, 
	Date_of_birth		date NOT NULL,
	FOREIGN KEY (Airline_name) REFERENCES Airline(Name),
	PRIMARY KEY (Username, Airline_name)
);

CREATE TABLE Staff_phone_num (
	Username		varchar(255), 
	Phone_num		int NOT NULL,
	FOREIGN KEY (Username) REFERENCES Airline_Staff(Username),
	PRIMARY KEY (Username)
);
	
CREATE TABLE Staff_email (
	Username		varchar(255), 
	Email			varchar(255) NOT NULL,
	FOREIGN KEY (Username) REFERENCES Airline_Staff(Username),
	PRIMARY KEY (Username)
);

CREATE TABLE Flight (
	Airline_name		varchar(255),
	Flight_num		int, 
	Departure_time	time, 
	Departure_date	date, 
	Arrival_time		time NOT NULL, 
	Arrival_date		date NOT NULL, 
	Departure_airport_ID int NOT NULL,
	Arrival_airport_ID       int NOT NULL,
	Airplane_ID 	int NOT NULL,
	Base_ticket_price	int NOT NULL,
	Status			varchar(255) NOT NULL,
	FOREIGN KEY (Airline_name) REFERENCES Airline(Name),
	PRIMARY KEY (Airline_name, Flight_num, Departure_time, Departure_date)
);

CREATE TABLE Ticket (
	Ticket_ID		int AUTO_INCREMENT, 
	Email 			varchar(255),
	Airline_name		varchar(255),
	Flight_num		int, 
	Departure_time	time, 
	Departure_date	date, 
	FirstName 		varchar(255) NOT NULL,
	LastName 		varchar(255) NOT NULL,
	Date_of_birth 		date NOT NULL,
	Card_num		int NOT NULL, 
	Name_on_card	varchar(255) NOT NULL, 
	Expiration_date	date NOT NULL,
	Purchase_date	date NOT NULL,
	Purchase_time	time NOT NULL,
	Card_type		varchar(255) NOT NULL,
	FOREIGN KEY (Airline_name, Flight_num, Departure_time, Departure_date) REFERENCES Flight(Airline_name, Flight_num, Departure_time, Departure_date),
	FOREIGN KEY (Email) REFERENCES Customer(Email),
	PRIMARY KEY (Ticket_ID, Airline_name, Flight_num, Departure_time, Departure_date)
);


CREATE TABLE Buys (
	Ticket_ID 		int, 
	Email 			varchar(255),
	FOREIGN KEY (Ticket_ID) REFERENCES Ticket(Ticket_ID),
	FOREIGN KEY (Email) REFERENCES Customer(Email),
	PRIMARY KEY (Ticket_ID, Email)
);

CREATE TABLE Has_taken (
	Email			varchar(255),
	Airline_name		varchar(255), 
	Flight_num		int, 
	Departure_time	time, 
	Departure_date	date, 
	Rate			int NOT NULL, 
	Comment		varchar(255) NOT NULL,
	FOREIGN KEY (Email) REFERENCES Customer(Email),
	FOREIGN KEY (Airline_name, Flight_num, Departure_time, Departure_date) REFERENCES Flight(Airline_name, Flight_num, Departure_time, Departure_date),
	PRIMARY KEY (Email, Airline_name, Flight_num, Departure_time, Departure_date)
);
