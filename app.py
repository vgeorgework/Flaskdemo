import os
from flask import Flask, render_template, request, redirect
import mysql.connector as mysql


app = Flask(__name__)

def establish_connection():
    """
    gain connection
    """
    cnx = mysql.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        auth_plugin='mysql_native_password'
    )
    return cnx

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        con=establish_connection()
        cur = con.cursor()
        cur.execute("SHOW TABLES")
        if cur.fetchone():
            cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        else:
            cur.execute("CREATE TABLE users (name varchar(20), email varchar(40));")
            cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        con.commit()
        con.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    con=establish_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    userDetails=cur.fetchall()
    if len(userDetails) > 0:
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

