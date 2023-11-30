from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

def connect_to_db():
    """
    A function that creates a connection to db.
    """
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_ROOT_USER"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=3306
    )

@app.route('/<table_name>', methods=['POST'])
def add_data(table_name):
    """
    A function that adds a new user to db.
    """
    try:
        mysql_db = connect_to_db() #creates a connection to db
        mycursor = mysql_db.cursor() 
        input_name = request.json.get("name")
        checks_table = f"SHOW TABLES LIKE '{table_name}';" # checks if the given table is in db
        mycursor.execute(checks_table)
        result = mycursor.fetchone()
        if not result: #if the table is not in the db, it creates a new table
            new_table =f"CREATE TABLE `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL)"
            mycursor.execute(new_table)
        insert_name = f"INSERT INTO `{table_name}`(name) VALUES ('{input_name}')" 
        mycursor.execute(insert_name)
        mysql_db.commit()
        return f"User `{input_name}` was successfully added to the database with the id `{mycursor.lastrowid}`"
    except Exception as e:
        return str(e)


@app.route('/<table_name>', methods=['GET'])
def get_data(table_name):
    """
    A function that returns all the data in a table in db.
    """
    try:
        mysql_db = connect_to_db() # creates a connection to db
        mycursor = mysql_db.cursor()
        get_data = f"SELECT * FROM `{table_name}`" # gets data from db
        mycursor.execute(get_data)
        result = mycursor.fetchall()
        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)