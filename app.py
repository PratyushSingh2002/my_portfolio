from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection(host_name, user_name, user_password, database=None):
    """ Create a database connection and create database if it doesn't exist """
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            ssl_disabled=True
        )
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        print(f"Database '{database}' checked/created.")
        
        # Reconnect to the specific database
        connection.database = database
        
        # Create messages table if it doesn't exist
        create_messages_table_query = """
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_messages_table_query)
        print("Table 'messages' checked/created.")
        
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
    host = "localhost"  # Change this to your host
    user = "root"       # Change this to your MySQL username
    db_password = "Pratyush@123"  # Change this to your MySQL password
    database = "user_data"
    
    # Create connection and ensure database and table are created if they don't exist
    connection = create_connection(host, user, db_password, database)
    
    if connection:
        insert_message(connection, name, email, message)  # Call insert_message
        connection.close()
        
    return redirect(url_for('index', success="true"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
