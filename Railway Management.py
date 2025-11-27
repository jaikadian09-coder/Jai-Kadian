import mysql.connector as sql
from random import randint

con = sql.connect(host="localhost", user="root", password="root@123")
con.autocommit = True
cur = con.cursor()

# Create database and tables
print("Setting up the database...")
cur.execute("CREATE DATABASE IF NOT EXISTS IRCTC;")
cur.execute("USE IRCTC;")
cur.execute(
    "CREATE TABLE IF NOT EXISTS accounts ("
    "id INT PRIMARY KEY, "
    "pass VARCHAR(16), "
    "name VARCHAR(100), "
    "sex CHAR(1), "
    "age VARCHAR(3), "
    "dob DATE, "
    "ph_no CHAR(10));"
)
cur.execute(
    "CREATE TABLE IF NOT EXISTS tickets ("
    "id INT, "
    "PNR INT, "
    "train VARCHAR(25), "
    "doj DATE, "
    "tfr VARCHAR(100), "
    "tto VARCHAR(100));"
)
print("Database and tables setup complete.")



# Account Creation
def create_acc():
    print("Enter the details to create your account:")
    i = randint(1000, 10000)
    print("Your generated ID is: " + str(i))
    p = input("Enter your password: ")
    n = input("Enter your name: ")
    sex = input("Enter your gender (M/F/O): ").upper()
    age = input("Enter your age: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    ph = input("Enter your contact number: ")

    if len(ph) != 10 or not ph.isdigit():
        print("Invalid phone number! It must be a 10-digit number.")
        return

    s1 = "INSERT INTO accounts (id, pass, name, sex, age, dob, ph_no) VALUES (" + str(i) + ", '" + p + "', '" + n + "', '" + sex + "', " + age + ", '" + dob + "', '" + ph + "');"
    cur.execute(s1)
    print("Account created successfully! Now you can log in.")
    login()



# Log in to Account
def login():
    global a
    print("Log in to your account:")
    a = int(input("Enter your ID: "))
    b = input("Enter your password: ")

    s2 = "SELECT name FROM accounts WHERE id = " + str(a) + " AND pass = '" + b + "';"
    cur.execute(s2)
    result = cur.fetchone()

    if result:
        print("Welcome back, " + result[0] + "!")
        main_menu()
    else:
        print("Invalid ID or password! Please try again.")
        login_menu()



# Ticket Creation
def buy_ticket():
    print("Enter details for your journey:")
    i = a
    pnr = randint(100000, 1000000)
    print("Your PNR is " + str(pnr))
    train = input("Enter the name of the train: ")
    doj = input("Enter the date of your journey (YYYY-MM-DD): ")
    fr = input("Enter the Departing Station: ")
    to = input("Enter the Destination Station: ")

    s4 = "INSERT INTO tickets (id, PNR, train, doj, tfr, tto) VALUES (" + str(i) + ", " + str(pnr) + ", '" + train + "', '" + doj + "', '" + fr + "', '" + to + "');"
    cur.execute(s4)
    print("Ticket booked successfully!")
    main_menu()



# Ticket Checking
def show_ticket():
    pnr = int(input("Enter your PNR: "))
    s5 = "SELECT * FROM tickets WHERE pnr = " + str(pnr) + ";"
    cur.execute(s5)
    result = cur.fetchone()

    if result and result[0] == a:
        print("Train: " + result[2])
        print("Date of Journey: " + str(result[3]))
        print("From: " + result[4])
        print("To: " + result[5])
    else:
        print("Unauthorized or ticket not found!")
    main_menu()



# Request a Refund
def cancel_ticket():
    pnr = int(input("Enter the PNR number of the ticket: "))
    s2 = "SELECT id, pnr, train FROM tickets WHERE pnr = " + str(pnr) + ";"
    cur.execute(s2)
    result = cur.fetchone()

    if result and result[0] == a:
        print("PNR: " + str(result[1]))
        print("Train: " + result[2])
        confirm = input("Do you really want to cancel this ticket? (Y/N): ").upper()
        if confirm == "Y":
            s3 = "DELETE FROM tickets WHERE pnr = " + str(pnr) + ";"
            cur.execute(s3)
            print("Ticket canceled! Refund will be processed shortly.")
    else:
        print("Unauthorized or ticket not found!")
    main_menu()



# Main Menu
def main_menu():
    print("What would you like to do today?")
    print("1. Purchase a Ticket")
    print("2. Check Ticket Status")
    print("3. Request a Refund")
    print("4. Account Settings")
    print("5. Logout")
    print("6. Exit")
    ch1 = int(input("Enter your choice: "))
    if ch1 == 1:
        buy_ticket()
    elif ch1 == 2:
        show_ticket()
    elif ch1 == 3:
        cancel_ticket()
    elif ch1 == 4:
        account()
    elif ch1 == 5:
        login_menu()
    else:
        print("Thank you for using the IRCTC portal!")



# Account Settings
def account():
    print("1. Show Account Details")
    print("2. Delete Account")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        s4 = "SELECT * FROM accounts WHERE id = " + str(a) + ";"
        cur.execute(s4)
        result = cur.fetchone()
        print("ID: " + str(result[0]))
        print("Name: " + result[2])
        print("Gender: " + result[3])
        print("Age: " + result[4])
        print("DOB: " + str(result[5]))
        print("Phone Number: " + result[6])
    elif ch == 2:
        confirm = input("Are you sure you want to delete your account? (Y/N): ").upper()
        if confirm == "Y":
            s6 = "DELETE FROM accounts WHERE id = " + str(a) + ";"
            cur.execute(s6)
            print("Account deleted successfully!")
            login_menu()
    main_menu()



# Login Menu
def login_menu():
    print("WELCOME TO THE IRCTC PORTAL")
    print("1. Create New Account")
    print("2. Log In")
    print("3. Exit")
    opt = int(input("Enter your choice: "))
    if opt == 1:
        create_acc()
    elif opt == 2:
        login()
    elif opt == 3:
        print("Thank you for using the IRCTC portal!")
    else:
        print("Invalid choice! Please try again.")
        login_menu()
   
       
# Start the program
if __name__ == "__main__":
    login_menu()
