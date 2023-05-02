#Import Flask Library
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

#Define route for login
@app.route('/login')
def login():
	return render_template('login.html')

#Define route for customer login
@app.route('/customer_login')
def customer_login():
	return render_template('customer_login.html')

#Define route for login
@app.route('/as_login')
def as_login():
	return render_template('as_login.html')

#Define route for register
@app.route('/register')
def register():
	return render_template('register.html')

#Define route for customer registration
@app.route('/customer_reg')
def customer_reg():
	return render_template('customer_reg.html')

#Define route for airline staff registration
@app.route('/as_reg')
def as_reg():
	return render_template('as_reg.html')


#Authenticates the login for customer
@app.route('/loginAuth_cust', methods=['GET', 'POST'])
def loginAuth_cust():
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
		session['Email'] = data['FirstName']
		return redirect(url_for('customer_home'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)

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
		#session is a built in
		session['Username'] = data['FirstName']
		return redirect(url_for('home'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)

#Authenticates the registration for customer
@app.route('/registerAuth_cust', methods=['GET', 'POST'])
def registerAuth_cust():
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
        error = "This customer already exists"
        return render_template('customer_reg.html', error = error)
    else:
        ins = 'INSERT INTO Customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (Email, Password, FirstName, LastName, Building_num, Street_name, Apartment_num, City, State, Zip_code, Passport_num, Passport_expiration, Passport_country, Date_of_birth))
        conn.commit()
        cursor.close()
        return render_template('customer_home.html')
    
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


@app.route('/home')
def home():
    
	username = None
	if 'username' in session:
		username = session['username']
	cursor = conn.cursor()
	query = 'SELECT * FROM Flight'
	cursor.execute(query)
	data1 = cursor.fetchall() 
	cursor.close()
	return render_template('home.html', username=username, flights=data1)

@app.route('/customer_home')
def customer_home():
    
	email = None
	if 'email' in session:
		email = session['email']
	cursor = conn.cursor()
	query1 = 'SELECT * FROM Buys WHERE Email = %s'
	# query1 = 'SELECT Ticket_ID FROM Buys'
	cursor.execute(query1, (email))
	data1 = cursor.fetchall()
	# query2 = 'SELECT * From Ticket WHERE Ticket_ID = %s'
	# cursor.execute(query2, (data1))
	# data2 = cursor.fetchall()
	cursor.close()
	return render_template('customer_home.html', email=email, flights=data1)
		
@app.route('/book', methods=['GET', 'POST'])
def post():
	cursor = conn.cursor()
	source = request.form['source']
	destination = request.form['destination']
	depart = request.form['depart']
	ret = request.form['return']
	query = 'SELECT * FROM Flight JOIN Airport ON Flight.Departure_Airport = Airport.Airport_ID WHERE name = %s'
	cursor.execute(query, (source))
	search = cursor.fetchall()
	conn.commit()
	cursor.close()
	return redirect(url_for('home', search=search))

@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')
		
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
