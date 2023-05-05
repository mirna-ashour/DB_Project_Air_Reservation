#Import Flask Library
from datetime import date, datetime, timedelta
from flask import Flask, render_template, request, session, url_for, redirect, flash
import pymysql.cursors

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
		            #    port = 8889,
                       user='root',
                       password='',
                       db='Airline_Reservation',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/', methods=['GET', 'POST'])
def hello():
	cursor = conn.cursor()
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
		return render_template('index.html', going=going, returning=returning, trip_type=trip_type)
	going = 'None'
	returning = 'None'
	trip_type = 'None'
	return render_template('index.html', going=going, returning=returning, trip_type=trip_type)

# @app.route('/index')
# def index():
	# cursor = conn.cursor()
	# if request.method == 'POST':
	# 	source_city = request.form['source_city']
	# 	destination_city = request.form['destination_city']
	# 	source_airp = request.form['source_airp']
	# 	destination_airp = request.form['destination_airp']
	# 	depart_date = request.form['depart']
	# 	return_date = request.form['return']
	# 	trip_type = request.form['options']
	# 	if depart_date != '' and return_date != '':
	# 		if source_city != '':
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
	# 			cursor.execute(query3, (source_city, destination_city, depart_date, return_date))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
	# 				cursor.execute(query4, (source_city, destination_city, depart_date, return_date))
	# 				returning = cursor.fetchall()
	# 		else:
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
	# 			cursor.execute(query3, (source_airp, destination_airp, depart_date, return_date))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s) AND (Arrival_date = %s)'
	# 				cursor.execute(query4, (source_airp, destination_airp, depart_date, return_date))
	# 				returning = cursor.fetchall()
	# 	elif depart_date != '':
	# 		if source_city != '':
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s)'
	# 			cursor.execute(query3, (source_city, destination_city, depart_date))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s) AND (Departure_date = %s)'
	# 				cursor.execute(query4, (source_city, destination_city, depart_date))
	# 				returning = cursor.fetchall()
	# 		else:
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s)'
	# 			cursor.execute(query3, (source_airp, destination_airp, depart_date))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s) AND (Departure_date = %s)'
	# 				cursor.execute(query4, (source_airp, destination_airp, depart_date))
	# 				returning = cursor.fetchall()
	# 	elif return_date != '':
	# 		if source_city != '':
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s) AND (Arrival_date = %s)'
	# 			cursor.execute(query3, (source_city, destination_city, return_date))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s) AND Arrival_date = %s)'
	# 				cursor.execute(query4, (source_city, destination_city, return_date))
	# 				returning = cursor.fetchall()
	# 		else:
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s) AND (Arrival_date = %s)'
	# 			cursor.execute(query3, (source_airp, destination_airp, return_date))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s) AND Arrival_date = %s)'
	# 				cursor.execute(query4, (source_airp, destination_airp, return_date))
	# 				returning = cursor.fetchall()
	# 	else:
	# 		if source_city != '':
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.City = %s)'
	# 			cursor.execute(query3, (source_city, destination_city))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.City = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.City = %s)'
	# 				cursor.execute(query4, (source_city, destination_city))
	# 				returning = cursor.fetchall()
	# 		else:
	# 			query3 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Departure_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Arrival_airport_ID = B.Airport_ID AND B.Name = %s)'
	# 			cursor.execute(query3, (source_airp, destination_airp))
	# 			going = cursor.fetchall()
	# 			returning = 'None'
	# 			if trip_type == 'option2': # trip_type = roundtrip
	# 				query4 = 'SELECT * From (Flight as F JOIN Airport as A JOIN Airport as B) WHERE (F.Arrival_airport_ID = A.Airport_ID AND A.Name = %s) AND (F.Departure_airport_ID = B.Airport_ID AND B.Name = %s)'
	# 				cursor.execute(query4, (source_airp, destination_airp))
	# 				returning = cursor.fetchall()
	# 	conn.commit()
	# 	cursor.close()
	# 	return render_template('index.html', going=going, returning=returning, trip_type=trip_type)		
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
		session['username'] = Email
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
	if 'username' in session:
		email = session['username']
	cursor = conn.cursor()
	# find upcoming flights
	today_date = date.today()
	time = datetime.now().strftime("%H:%M:%S")
	query = 'SELECT * From Ticket WHERE Email = %s AND Departure_date > %s OR (Departure_date = %s AND Departure_time > %s)'
	cursor.execute(query, (email, today_date, today_date, time))
	data = cursor.fetchall()
	# find past flights
	query_past = 'SELECT * From Ticket WHERE Email = %s AND Departure_date < %s OR (Departure_date = %s AND Departure_time < %s) '
	cursor.execute(query_past, (email, today_date, today_date, time))
	past_flight = cursor.fetchall()
	# find first name of customer
	query2 = 'SELECT FirstName From Customer WHERE Email = %s'
	cursor.execute(query2, (email))
	data2 = cursor.fetchone()
	# find customer's tickets
	query5 = 'SELECT * From Ticket WHERE Email = %s'
	cursor.execute(query5, (email))
	ticket = cursor.fetchall()
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
		return render_template('cus_home.html', firstname=data2, future_flights=data, past_flights=past_flight, ticket=ticket, going=going, returning=returning, trip_type=trip_type)		
	else:
		going = 'None'
		returning = 'None'
		trip_type = 'None'
		conn.commit()
		cursor.close()
		return render_template('cus_home.html', firstname=data2, future_flights=data, past_flights=past_flight, ticket=ticket, going=going, returning=returning, trip_type=trip_type)

# customer rate/comment route
@app.route('/rate_comment', methods =['GET', 'POST'])
def rate_comment():
	if request.method=='POST':
		Rating = request.form['Rating']
		Comment = request.form['Comment']
	cursor = conn.cursor(0)
	Email = 'None'
	if 'username' in session:
		Email = session['username']
	Airline_name = request.args.get('Airline_name')
	Flight_num = request.args.get('Flight_num')
	Departure_time = request.args.get('Departure_time')
	Departure_date = request.args.get('Departure_date')
	query = 'INSERT INTO Has_taken VALUES (%s, %s, %s, %s, %s, %s, %s)'
	cursor.execute(query, (Email, Airline_name, Flight_num, Departure_time, Departure_date, Rating, Comment))
	flash("Rating and comment successfully recorded.")
	return redirect(url_for('cus_home'))


# customer delete ticket route
@app.route('/delete', methods=['GET', 'POST'])
def delete():
	Email = 'None'
	if 'username' in session:
		Email = session['username']
	cursor = conn.cursor()
	Airline_name = request.args.get('Airline_name')
	Flight_num = request.args.get('Flight_num')
	Departure_time = request.args.get('Departure_time')
	Departure_date = request.args.get('Departure_date')
	# check if flight is more than 24 hours out*****
	depart_date = date(int(Departure_date[0:4]), int(Departure_date[5:7]), int(Departure_date[8:10]))
	depart_time = datetime.strptime(Departure_time, '%H:%M:%S')
	today = date.today()
	tomorrow = today + timedelta(days=1)
	time = datetime.now().strftime("%H:%M:%S")
	current_time = datetime.strptime(time, '%H:%M:%S')
	if ((today <= depart_date <= tomorrow)):
		if ((depart_date == tomorrow) and (depart_time <= current_time)):
			flash("Cannot delete ticket- flight is less than 24 hours out.")
			return redirect(url_for('cus_home'))
	# *********
	query = 'DELETE FROM Ticket WHERE Email = %s AND Airline_name = %s AND Flight_num = %s AND Departure_time = %s AND Departure_date = %s'
	cursor.execute(query, (Email, Airline_name, Flight_num, Departure_time, Departure_date))
	flash("Ticket successfully deleted")
	return redirect(url_for('cus_home'))

# Customer purchase ticket route
@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
	if request.method=='POST':
		FirstName = request.form['FirstName']
		LastName = request.form['LastName']
		Date_of_birth = request.form['Date_of_birth']
		Card_num = request.form['Card_num']
		Name_on_card = request.form['Name_on_card']
		Expiration_date = request.form['Expiration_date']
		Card_type = request.form['Card_type']
	cursor = conn.cursor()
	Email = 'None'
	if 'username' in session:
		Email = session['username']
	Airline_name = request.args.get('Airline_name')
	Flight_num = request.args.get('Flight_num')
	Departure_time = request.args.get('Departure_time')
	Departure_date = request.args.get('Departure_date')
	Purchase_date = date.today()
	time = datetime.now()
	Purchase_time = time.strftime("%H:%M:%S")
	query = 'INSERT INTO Ticket(Email, Airline_name, Flight_num, Departure_time, Departure_date, FirstName, LastName, Date_of_birth, Card_num, Name_on_card, Expiration_date, Purchase_date, Purchase_time, Card_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
	cursor.execute(query, (Email, Airline_name, Flight_num, Departure_time, Departure_date, FirstName, LastName, Date_of_birth, Card_num, Name_on_card, Expiration_date, Purchase_date, Purchase_time, Card_type))
	flash("Ticket successfully purchased")
	return redirect(url_for('cus_home'))


# Customer track spending route
@app.route('/track_spending', methods=['GET', 'POST'])
def track_spending():
	Email = 'None'
	if 'username' in session:
		Email = session['username']
	cursor = conn.cursor()
	if request.method == 'POST':
		from_date = request.form['from']
		until_date = request.form['until']
	else:
		# default is total money spent for last year
		until_date_bef = date.today()
		from_date = until_date_bef - timedelta(days=365)
		until_date = str(until_date_bef)
	query = 'SELECT sum(Base_ticket_price) FROM Flight as F NATURAL JOIN Ticket as T WHERE T.Email = %s AND T.Purchase_date >= %s AND T.Purchase_date <= %s'
	cursor.execute(query, (Email, from_date, until_date))
	total_cost = cursor.fetchone()
	if total_cost['sum(Base_ticket_price)'] == None:
		total_cost['sum(Base_ticket_price)'] = 0
	# find cost for each month in the last six months
	data_over_months = []
	curr_date = date(int(until_date[0:4]), int(until_date[5:7]), int(until_date[8:10]))
	if request.method == 'GET':
		for i in range(6):
			first_of_currmonth = curr_date.replace(day=1)
			next_month = curr_date.replace(day=28) + timedelta(days=4)
			last_of_currmonth = next_month - timedelta(days=next_month.day)
			query = 'SELECT sum(Base_ticket_price) FROM Flight as F NATURAL JOIN Ticket as T WHERE T.Email = %s AND T.Purchase_date >= %s AND T.Purchase_date <= %s'
			cursor.execute(query, (Email, first_of_currmonth, last_of_currmonth))
			sum_for_month = cursor.fetchone()
			if sum_for_month['sum(Base_ticket_price)'] == None:
				sum_for_month['sum(Base_ticket_price)'] = 0
			curr_month = last_of_currmonth.month
			data_over_months.append((curr_month, sum_for_month['sum(Base_ticket_price)']))
			curr_date = first_of_currmonth - timedelta(days=18)
	else:
		end_date = date(int(from_date[0:4]), int(from_date[5:7]), int(from_date[8:10])).replace(day=1)
		first_of_currmonth = curr_date.replace(day=1)
		while first_of_currmonth != end_date:
			first_of_currmonth = curr_date.replace(day=1)
			next_month = curr_date.replace(day=28) + timedelta(days=4)
			last_of_currmonth = next_month - timedelta(days=next_month.day)
			query = 'SELECT sum(Base_ticket_price) FROM Flight as F NATURAL JOIN Ticket as T WHERE T.Email = %s AND T.Purchase_date >= %s AND T.Purchase_date <= %s'
			cursor.execute(query, (Email, first_of_currmonth, last_of_currmonth))
			sum_for_month = cursor.fetchone()
			if sum_for_month['sum(Base_ticket_price)'] == None:
				sum_for_month['sum(Base_ticket_price)'] = 0
			curr_month = last_of_currmonth.month
			data_over_months.append((curr_month, sum_for_month['sum(Base_ticket_price)']))
			curr_date = first_of_currmonth - timedelta(days=18)

	return render_template('track_spending.html', total_cost=total_cost, data_over_months=data_over_months, from_date=from_date, until_date=until_date)



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
@app.route('/staff/view_flights')
def view_flights():
	return render_template('staff/view_flights.html')

#AS view flights form authentication 
@app.route('/staff/view_flights_auth', methods=['GET', 'POST'])
def view_flights_auth():
	return render_template('staff/view_flights.html')

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
	statusUpdate = request.form['newStatus'] 	#should make this a radio button

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
	age = request.form['age'] 		#maybe we should do a function that calculates this? -> yes 

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

@app.route('/staff/flight_ratings')
def flight_ratings():
	return render_template('/staff/flight_ratings.html')
 
@app.route('/staff/flight_ratings_auth', methods=['GET', 'POST'])
def flight_ratings_auth():
	error = None
	showRatings = False
	flightNum = request.form['flightNum']
	departureDate = request.form['departureDate']
	departureTime = request.form['departureTime']
	showRatings = request.form['showRatings']
	airline = session['airline']

	cursor = conn.cursor()
	query1 = 'SELECT Flight_num, avg(Rate) as Avg_rating FROM Has_taken WHERE Airline_name = %s AND Flight_num = %s AND Departure_date = %s AND Departure_time = %s GROUP BY Flight_num'
	cursor.execute(query1, (airline, flightNum, departureDate, departureTime))
	data1 = cursor.fetchall()
	data2 = None

	if(data1):
		if(showRatings == "true"):
			query2 = 'SELECT FirstName, LastName, Email, Rate, Comment FROM Has_taken NATURAL JOIN Customer WHERE Airline_name = %s AND Flight_num = %s AND Departure_date = %s AND Departure_time = %s' 
			cursor.execute(query2, (airline, flightNum, departureDate, departureTime))
			data2 = cursor.fetchall()
	else:
		error = "There are no ratings for the given flight number."

	return render_template('staff/flight_ratings.html', avg_rating=data1, all_ratings=data2, error=error)

#CONFUSION WITH BUYS TABLE AND EMAILS 
@app.route('/staff/freq_cust', methods=['GET', 'POST'])
def freq_cust():
	error = None
	airline = session['airline']
	data1 = None

	today = date.today()
	this_year = today.year
	this_year_start = date(this_year, 1, 1)

	cursor = conn.cursor()
	createView = "CREATE VIEW view_ticket_num AS (SELECT Email, count(Ticket_ID) as num_tickets FROM Ticket WHERE Airline_name = %s AND Purchase_date >= %s GROUP BY Email)"
	cursor.execute(createView, (airline, this_year_start))
	query1 = "SELECT Email, MAX(num_tickets) as max_num_tickets FROM view_ticket_num"
	cursor.execute(query1)
	data1 = cursor.fetchall()
	deleteView = "DROP view view_ticket_num"
	cursor.execute(deleteView)

	if(request.method == 'POST'):
		custEmail = request.form['email']
		cursor = conn.cursor()
		query2 = "SELECT Flight_num, FirstName, LastName, Email FROM Ticket NATURAL JOIN Flight WHERE Airline_name = %s AND Email = %s AND Arrival_date < %s"
		cursor.execute(query2, (airline, custEmail, today))
		data2 = cursor.fetchall()
		conn.commit()
		cursor.close()

		if(data2):
			return render_template('staff/freq_cust.html', most_freq=data1, cust_flights=data2, email=custEmail, error=error)
		error = "There are no flights to view for this customer."
	return render_template('staff/freq_cust.html', most_freq=data1, error=error, cust_flights=None)

#WORKS
@app.route('/staff/reports', methods=['GET', 'POST'])
def reports():
	error = None
	if request.method == 'POST':
		startDate = request.form['startDate']
		endDate = request.form['endDate']
		airline = session['airline']

		cursor = conn.cursor()
		query = "SELECT count(Ticket_ID) as num_tickets FROM Ticket WHERE Airline_name = %s AND Purchase_date >= %s AND Purchase_date <= %s GROUP BY Airline_name"
		cursor.execute(query, (airline, startDate, endDate))
		data = cursor.fetchone()
		conn.commit()
		cursor.close()
		if(data):
			return render_template('staff/reports.html', num_tickets=data['num_tickets'], error=error)
		else:
			error = "No tickets found in that range."
			return render_template('staff/reports.html', error=error)
	else:
		return render_template('staff/reports.html', error=error, num_tickets='')

@app.route('/staff/revenue')
def revenue():
	error = None
	airline = session['airline']

	today = date.today()
	'''lastMonth = today - timedelta(days=30)
	lastYear = today - timedelta(days=365)'''

	one_month_ago = today.month - 1
	last_month = date(today.year, one_month_ago, today.day)
	one_year_ago = today.year - 1
	last_year = date(one_year_ago, today.month, today.day)

	#SELECT (count(Ticket_ID) * Base_ticket_price) as price_each_flight FROM Ticket NATURAL JOIN Flight WHERE Airline_name = %s AND Purchase_date >= %S AND Purchase_date <= %s GROUP BY Flight_num
	#SELECT sum(price_each_flight) FROM (subquery) GROUP BY 
	# SELECT sum(Base_ticket_price) as revenue FROM Ticket NATURAL JOIN Flight WHERE Airline_name = %s AND Purchase_date >= %S AND Purchase_date <= %s
	cursor = conn.cursor()
	query1 = "SELECT sum(Base_ticket_price) as revenue FROM Flight WHERE Airline_name = %s AND Purchase_date >= %s AND Purchase_date <= %s GROUP BY Airline_name"
	cursor.execute(query1, (airline, last_month, today))
	data1 = cursor.fetchone()
	conn.commit()
	cursor.close()

	query2 = "SELECT sum(Base_ticket_price) as revenue FROM Flight WHERE Airline_name = %s AND Purchase_date >= %s AND Purchase_date <= %s GROUP BY Airline_name"
	cursor.execute(query2, (airline, last_year, today))
	data2 = cursor.fetchone()
	conn.commit()
	cursor.close()

	if(data1 and data2):
		return render_template('staff/revenue.html', revenueMonth=data1['revenue'], revenueYear=data2['revenue'])
	elif( (data1 == None) and data2):
		return render_template('staff/revenue.html', revenueMonth=0, revenueYear=data2['revenue'])
	else:
		return render_template('staff/revenue.html', revenueMonth=0, revenueYear=0)

		
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 4000, debug = True)
