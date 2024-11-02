from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection(host_name, user_name, user_password, database=None):
    """ Create a database connection to a MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database,  # Include database here if specified
            ssl_disabled=True  # Disable SSL for the connection
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def insert_message(connection, name, email, message):
    """ Insert a new message into the messages table """
    cursor = connection.cursor()
    query = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (name, email, message))
        connection.commit()  # Commit the transaction
        print("Message added to database.")
    except Error as e:
        print(f"The error '{e}' occurred while inserting message data")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    email = request.form['Mail']
    message = request.form['Message']
    
    # Database connection details
    host = "192.168.87.220"
    user = "pratyush"
    password = "b(ZDQyPfB8T8/j!Y"
    database = "user_data"
    
    connection = create_connection(host, user, password, database)
    
    if connection:
        insert_message(connection, name, email, message)  # Call insert_message
        connection.close()
        
    return "User registered successfully!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
