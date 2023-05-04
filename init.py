#Import Flask Library
from datetime import date, datetime
from flask import Flask, render_template, request, session, url_for, redirect, flash
import pymysql.cursors

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
		               port = 8889,
                       user='root',
                       password='root',
                       db='Airline_Reservation',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
	return render_template('index.html')


								##################################### LOGIN AND REGISTRATION CODE ##############################################

#General login page route
@app.route('/login')
def login():
	return render_template('login.html')

#Logout function route
@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')

#Customer login route
@app.route('/cus_login')
def cus_login():
	return render_template('cus_login.html')

#Authenticates the login for customer
@app.route('/loginAuth_cus', methods=['GET', 'POST'])
def loginAuth_cus():
	#grabs information from the forms
	Email = request.form['Email']
	Password = request.form['Password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Customer WHERE Email = %s and Password = %s'
	cursor.execute(query, (Email, Password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['Email'] = Email
		session['type'] = "cust"
		return redirect(url_for('cus_home'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)

#Airline staff login route
@app.route('/as_login')
def as_login():
	return render_template('as_login.html')


#Authenticates the login for airline staff
@app.route('/loginAuth_as', methods=['GET', 'POST'])
def loginAuth_as():
	#grabs information from the forms
	Username = request.form['Username']
	Password = request.form['Password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Airline_Staff WHERE Username = %s and Password = %s'
	cursor.execute(query, (Username, Password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		session['username'] = data['Username']
		session['firstName'] = data['First_name']
		session['airline'] = data['Airline_name']
		session['type'] = "staff"
		return redirect(url_for('as_home'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)




#General regsiter page
@app.route('/register')
def register():
	return render_template('register.html')

#Customer registration route
@app.route('/cus_reg')
def cus_reg():
	return render_template('cus_reg.html')

#Authenticates the registration for customer
@app.route('/registerAuth_cus', methods=['GET', 'POST'])
def registerAuth_cus():
	#grabs information from the forms
	Email = request.form['Email']
	Password = request.form['Password']
	FirstName = request.form['FirstName']
	LastName = request.form['LastName']
	Building_num = request.form['Building_num']
	Street_name = request.form['Street_name']
	Apartment_num = request.form['Apartment_num']
	City = request.form['City']
	State = request.form['State']
	Zip_code = request.form['Zip_code']
	Passport_num = request.form['Passport_num']
	Passport_expiration = request.form['Passport_expiration']
	Passport_country = request.form['Passport_country']
	Date_of_birth = request.form['Date_of_birth']

    #cursor used to send queries
	cursor = conn.cursor()
    #executes query
	query = 'SELECT * FROM Customer WHERE Email = %s'
	cursor.execute(query, (Email))
    #stores the results in a variable
	data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
        #If the previous query returns data, then user exists
		flash("This customer already exists")
		return render_template('cus_reg.html')
	else:
		ins = 'INSERT INTO Customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (Email, Password, FirstName, LastName, Building_num, Street_name, Apartment_num, City, State, Zip_code, Passport_num, Passport_expiration, Passport_country, Date_of_birth))
		conn.commit()
		cursor.close()
		error = "You have been successfully registered! Please login now."
		return render_template('cus_login.html', error=error)




#Airline staff registration route
@app.route('/as_reg')
def as_reg():
	return render_template('as_reg.html')

#Authenticates the registration for airline staff
@app.route('/registerAuth_as', methods=['GET', 'POST'])
def registerAuth_as():
	#grabs information from the forms
	Username = request.form['Username']
	Airline_name = request.form['Airline_name']
	Password = request.form['Password']
	First_name = request.form['First_name']
	Last_name = request.form['Last_name']
	Date_of_birth = request.form['Date_of_birth']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Airline_Staff WHERE Username = %s and Airline_name = %s'
	cursor.execute(query, (Username, Airline_name))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This airline staff member already exists"
		return render_template('as_reg.html', error = error)
	else:
		ins = 'INSERT INTO Airline_Staff VALUES(%s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (Username, Airline_name, Password, First_name, Last_name, Date_of_birth))
		conn.commit()
		cursor.close()
		return render_template('index.html')   # CHANGE


	
									######################################## CUSTOMER CODE ################################################

#General home page for customers
@app.route('/cus_home', methods =['GET', 'POST']) #, methods =['GET', 'POST']
def cus_home():
	email = 'None'
	if 'Email' in session:
		email = session['Email']
	cursor = conn.cursor()
	query = 'SELECT * From Ticket WHERE Ticket_ID in (SELECT Ticket_ID FROM Buys WHERE Email = %s)'
	cursor.execute(query, (email))
	data = cursor.fetchall()
	query2 = 'SELECT FirstName From Customer WHERE Email = %s'
	cursor.execute(query2, (email))
	data2 = cursor.fetchone()
	query = 'SELECT*'
	if request.method == 'POST':			
		source_city = request.form['source_city']
		destination_city = request.form['destination_city']
		source_airp = request.form['source_airp']
		destination_airp = request.form['destination_airp']
		depart_date = request.form['depart']
		return_date = request.form['return']
		trip_type = request.form['options']
		if depart_date != '' and return_date != '':
			if source_city != '':
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
				cursor.execute(query3, (source_city, destination_city, depart_date, return_date))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
					cursor.execute(query4, (source_city, destination_city, depart_date, return_date))
					returning = cursor.fetchall()
			else:
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
				cursor.execute(query3, (source_airp, destination_airp, depart_date, return_date))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
					cursor.execute(query4, (source_airp, destination_airp, depart_date, return_date))
					returning = cursor.fetchall()
		elif depart_date != '':
			if source_city != '':
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s)'
				cursor.execute(query3, (source_city, destination_city, depart_date))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s)'
					cursor.execute(query4, (source_city, destination_city, depart_date))
					returning = cursor.fetchall()
			else:
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s)'
				cursor.execute(query3, (source_airp, destination_airp, depart_date))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s)'
					cursor.execute(query4, (source_airp, destination_airp, depart_date))
					returning = cursor.fetchall()
		elif return_date != '':
			if source_city != '':
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s) AND (Arrival_date = %s)'
				cursor.execute(query3, (source_city, destination_city, return_date))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s) AND Arrival_date = %s)'
					cursor.execute(query4, (source_city, destination_city, return_date))
					returning = cursor.fetchall()
			else:
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s) AND (Arrival_date = %s)'
				cursor.execute(query3, (source_airp, destination_airp, return_date))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s) AND Arrival_date = %s)'
					cursor.execute(query4, (source_airp, destination_airp, return_date))
					returning = cursor.fetchall()
		else:
			if source_city != '':
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s)'
				cursor.execute(query3, (source_city, destination_city))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s)'
					cursor.execute(query4, (source_city, destination_city))
					returning = cursor.fetchall()
			else:
				query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s)'
				cursor.execute(query3, (source_airp, destination_airp))
				going = cursor.fetchall()
				returning = 'None'
				if trip_type == 'option2': # trip_type = roundtrip
					query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s)'
					cursor.execute(query4, (source_airp, destination_airp))
					returning = cursor.fetchall()
		conn.commit()
		cursor.close()
		return render_template('cus_home.html', firstname=data2, flights=data, going=going, returning=returning, trip_type=trip_type)		
	else:
		going = 'None'
		returning = 'None'
		trip_type = 'None'
		conn.commit()
		cursor.close()
		return render_template('cus_home.html', firstname=data2, flights=data, going=going, returning=returning, trip_type=trip_type)

# #Customer purchase ticket route
@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
	if request.method == 'POST':
		Airline_name = request.form['Airline_name']
		Flight_num = request.form['Flight_num']
		Departure_time = request.form['Departure_time']
		Departure_date = request.form['Departure_date']
		FirstName = request.form['FirstName']
		LastName = request.form['LastName']
		Date_of_birth = request.form['Date_of_birth']
		Card_num = request.form['Card_num']
		Name_on_card = request.form['Name_on_card']
		Expiration_date = request.form['Expiration_date']
		Card_type = request.form['Card_type']
		Purchase_date = date.today()
		time = datetime.now()
		Purchase_time = time.strftime("%H:%M:%S")
		cursor = conn.cursor()
		query = 'INSERT INTO Ticket(Airline_name, Flight_num, Departure_time, Departure_date, FirstName, LastName, Date_of_birth, Card_num, Name_on_card, Expiration_date, Purchase_date, Purchase_time, Card_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(query, (Airline_name, Flight_num, Departure_time, Departure_date, FirstName, LastName, Date_of_birth, Card_num, Name_on_card, Expiration_date, Purchase_date, Purchase_time, Card_type))
		conn.commit()
		cursor.close()
		flash("Ticket successfully purchased")
		return redirect(url_for('cus_home'))
	return render_template('purchase.html')


# @app.route('/book', methods=['GET', 'POST'])
# def post():
# 	cursor = conn.cursor()
# 	source = request.form['source']
# 	destination = request.form['destination']
# 	depart = request.form['depart']
# 	ret = request.form['return']
# 	query = 'SELECT * FROM Flight JOIN Airport ON Flight.Departure_Airport = Airport.Airport_ID WHERE name = %s'
# 	cursor.execute(query, (source))
# 	search = cursor.fetchall()
# 	conn.commit()
# 	cursor.close()
# 	return redirect(url_for('home', search=search))

								######################################### AIRLINE STAFF CODE #############################################

#Airline staff home page
@app.route('/as_home', methods=['GET', 'POST'])
def as_home():

	name = None
	if 'firstName' in session:
		print(session['firstName'])
		name = session['firstName']
		
	return render_template('as_home.html', name=name)

#AS view flights form 
@app.route('/staff/view_flights', methods=['GET', 'POST'])
def view_flights():
	return render_template('staff/view_flights.html')

#AS view flights form authentication 

	#MISSING. NOT YET CREATED ^^

#AS create flight form 
@app.route('/staff/create_flight') 
def create_flights():
	return render_template('staff/create_flight.html')

#AS create flight form authentication 
@app.route('/create_flight_auth', methods=['GET', 'POST']) 
def create_flight_auth():
	departure = request.form['departure']
	arrival = request.form['arrival'] 
	flightNum = request.form['flightNum']
	airplaneID = request.form['airplane']
	departDate = request.form['departDate'] 
	departTime = request.form['departTime'] 
	arriveDate = request.form['arriveDate'] 
	arriveTime = request.form['arriveTime'] 
	basePrice = request.form['basePrice']
	status = "on-time"
	airline = session['airline']

	cursor = conn.cursor()

	#validating airplane number (with the airline it belongs to)
	query = 'SELECT * FROM Airplane WHERE Airplane_ID = %s and Airline_name = %s'
	cursor.execute(query, (airplaneID, airline))
	data2 = cursor.fetchone()
	error = None
	if(data2):
		#airplane exists and with the correct airline
		query = 'INSERT INTO Flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		values = (airline, flightNum, departTime, departDate, arriveTime, arriveDate, airplaneID, departure, arrival, basePrice, status)
		cursor.execute(query, values)
		conn.commit()
		cursor.close()
		return render_template('staff/create_flight.html')
	else:
		error = 'This airplane does not exist with your airline.'
		return render_template('staff/create_flight.html', error=error)

@app.route('/staff/change_status')
def change_status():
	return render_template('staff/change_status.html')

@app.route('/change_status_auth', methods=['GET', 'POST'])
def change_status_auth():
	flightNum = request.form['flightNum']
	airline = request.form['airlineName']
	departDate = request.form['departDate']
	departTime = request.form['departTime']
	statusUpdate = request.form['newStatus']

	cursor = conn.cursor()
	query = 'UPDATE Flight SET Status = %s WHERE Flight_num = %s AND Airline_name = %s AND Departure_date = %s AND Departure_time = %s'
	values = (statusUpdate, flightNum, airline, departDate, departTime)
	cursor.execute(query, values)
	conn.commit()
	cursor.close()
	return render_template('staff/change_status.html')

@app.route('/staff/add_airplane')
def add_airplane():
	return render_template('staff/add_airplane.html')

@app.route('/add_airplane_auth', methods=['GET', 'POST'])
def add_airplane_auth():
	cursor = conn.cursor()
	airline = session['airline']

	numOfSeats = request.form['numOfSeats']
	manufactureDate = request.form['manufactureDate']
	manufacturer = request.form['manufacturer']
	age = request.form['age'] #maybe we should do a function that calculates this?

	query = 'INSERT INTO Airplane VALUES(%s, %s, %s, %s, %s)'
	values = (airline, numOfSeats, manufacturer, manufactureDate, age)
	cursor.execute(query, values)
	conn.commit()
	cursor.close()
	return render_template('staff/add_airplane.html')

@app.route('/staff/add_airport')
def add_airport():
	return render_template('staff/add_airport.html')

@app.route('/add_airport_auth', methods=['GET', 'POST'])
def add_airport_auth():
	name = request.form['name']
	city = request.form['city']
	country = request.form['country']
	ap_type = request.form['ap_type']

	cursor = conn.cursor()
	query = 'INSERT INTO Airport VALUES(%s, %s, %s, %s)'
	values =(name, city, country, ap_type)
	cursor.execute(query, values)
	conn.commit()
	cursor.close()
	return render_template('staff/add_airport.html')

#PROBABLY NEED A FORM FOR SPECIFIC FLIGHT INSTEAD. QUERIES WILL BE EASIER
@app.route('/staff/flight_ratings_auth')
def flight_ratings_auth():
	return render_template('staff/flight_ratings.html')

@app.route('/staff/flight_ratings_auth')
def flight_ratings_auth():
	showRatings = False
	flightNum = request.form['flightNum']
	departureDate = request.form['departureDate']
	departureTime = request.form['departureTime']
	showRatings = request.form['showRatings']
	airline = session['airline']

	cursor = conn.cursor()
	query1 = 'SELECT Flight_num, avg(Rate) as Avg_rating FROM Has_taken WHERE Airline_name = %s AND Flight_num = %s AND Departure_date = %s AND Departure_time = %s GROUP BY Flight_num)'
	cursor.execute(query1, (airline, flightNum, departureDate, departureTime))
	data1 = cursor.fetchall()
	data2 = None

	if(showRatings == "true"):
		query2 = 'SELECT FirstName, LastName, Email, Rate, Comment FROM Has_taken NATURAL JOIN Customer WHERE Airline_name = %s AND Flight_num = %s AND Departure_date = %s AND Departure_time = %s)' 
		cursor.execute(query2, (airline, flightNum, departureDate, departureTime))
		data2 = cursor.fetchall()

	return render_template('staff/flight_ratings.html', avg_rating=data1, all_ratings=data2)

@app.route('/staff/freq_cust')
def freq_cust():
	return render_template('staff/freq_cust.html')

@app.route('/freq_cust_auth', methods=['GET', 'POST'])
def freq_cust_auth():
	return render_template('staff/freq_cust.html')

@app.route('/staff/reports')
def reports():
	return render_template('staff/reports.html')

@app.route('/reports_auth', methods=['GET', 'POST'])
def reports_auth():
	return render_template('staff/reports.html')

@app.route('/revenue')
def revenue():
	return render_template('staff/revenue.html')

@app.route('/revenue_auth', methods=['GET', 'POST'])
def revenue_auth():
	return render_template('staff/revenue.html')

"""
@app.route('/change_status', methods=['GET', 'POST'])
def change_status():
	flightNum = request.form['flightNum']
	airline = request.form['airlineName']
	departDate = request.form['departDate']
	departTime = request.form['departTime']
	statusUpdate = request.form['newStatus']

	cursor = conn.cursor()
	query = 'UPDATE Flight SET Status = %s WHERE Flight_num = %s AND Airline_name = %s AND Departure_date = %s AND Departure_time = %s'
	values = (statusUpdate, flightNum, airline, departDate, departTime)
	cursor.execute(query, values)
	conn.commit()
	cursor.close()
	return redirect(url_for('staff/change_status'))
"""

"""
@app.route('/staff/add_airport', methods=['GET', 'POST'])
def add_airport():
	name = request.form['name']
	city = request.form['city']
	country = request.form['country']
	ap_type = request.form['ap_type']

	cursor = conn.cursor()
	query = 'INSERT INTO Airport VALUES(%s, %s, %s, %s)'
	values =(name, city, country, ap_type)
	cursor.execute(query, values)
	conn.commit()
	cursor.close()
	return redirect(url_for('staff/add_airport'))
"""
"""
@app.route('/staff/add_airplane', methods=['GET', 'POST'])
def add_airplane():
	cursor = conn.cursor()

	username = session['uid']
	query = 'SELECT Airline_name FROM Airline_Staff WHERE Username=%s'
	cursor.execute(query, (username))
	data = cursor.fetchone()
	airline = data['Airline_name'] #!!!!

	numOfSeats = request.form['numOfSeats']
	manufactureDate = request.form['manufactureDate']
	manufacturer = request.form['manufacturer']
	age = request.form['age'] #maybe we should do a function that calculates this?

	query = 'INSERT INTO Airplane VALUES(%s, %s, %s, %s, %s)'
	values = (airline, numOfSeats, manufacturer, manufactureDate, age)
	cursor.execute(query, values)
	conn.commit()
	cursor.close()
	return redirect(url_for('staff/add_airplane'))
"""
		
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 4000, debug = True)
