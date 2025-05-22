from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
mydb = mysql.connector.connect(
    user='root',
    password='121212',
    host='localhost',
    database='hotel'
)
mycursor = mydb.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    addr = request.form['addr']
    indate = request.form['indate']
    outdate = request.form['outdate']
    sql = "INSERT INTO custdata (custname, addr, indate, outdate) VALUES (%s, %s, %s, %s)"
    val = (name, addr, indate, outdate)
    mycursor.execute(sql, val)
    mydb.commit()
    return render_template('success.html', message="Customer registered successfully!")

@app.route('/roomtype')
def roomtype():
    mycursor.execute("SELECT * FROM roomtype")
    rows = mycursor.fetchall()
    return render_template('roomtype.html', rooms=rows)

@app.route('/restaurant')
def restaurant_menu():
    mycursor.execute("SELECT * FROM restaurent")
    rows = mycursor.fetchall()
    return render_template('restaurant_menu.html', items=rows)

if __name__ == '__main__':
    app.run(debug=True)
