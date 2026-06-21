import mysql.connector
con = None

def connect():
    global con
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql",
        database="HEALTHCARE"
    )


def addDoctor():
    print("\n ADDING A NEW DOCTOR")
    Sl_NO = int(input("Enter Serial No: "))
    Dr_ID = input("Enter Doctor Id: ")
    Dr_Name = input("Enter Doctor Name: ")
    Specialisation = input("Enter Doctor Specialisation: ")
    DOJ = input("Enter Date of Joining: ")

    c1 = con.cursor()
    q = "INSERT INTO DOCTOR2 VALUES({}, '{}', '{}', '{}', '{}')".format(
        Sl_NO, Dr_ID, Dr_Name, Specialisation, DOJ
    )
    c1.execute(q)
    con.commit()
    print("Doctor details added successfully")


def showDoctors():
    print("\n SHOWING ALL DOCTOR DETAILS")
    c1 = con.cursor()
    c1.execute("SELECT * FROM DOCTOR2")
    rec = c1.fetchall()
    print("S.No   Dr_ID   Dr_Name   Specialisation   DOJ")
    for i in rec:
        print(i)


def delDoctor():
    print("\n DELETING DOCTOR DETAILS")
    did = input("Enter Doctor Id to delete: ")
    c1 = con.cursor()
    q = "DELETE FROM DOCTOR2 WHERE Dr_ID='{}'".format(did)
    c1.execute(q)
    con.commit()
    print("Doctor record deleted successfully")


def addPatient():
    print("\n ADDING A NEW PATIENT")
    Sl_NO = int(input("Enter Serial No: "))
    Pt_Code = input("Enter Patient Code: ")
    Pt_Name = input("Enter Patient Name: ")
    Health_Issue = input("Enter Patient's Health Issue: ")
    Gender = input("Enter Gender: ")
    Age = int(input("Enter Age: "))
    City = input("Enter City: ")

    c1 = con.cursor()
    q = "INSERT INTO PATIENT1 VALUES({}, '{}', '{}', '{}', '{}', {}, '{}')".format(
        Sl_NO, Pt_Code, Pt_Name, Health_Issue, Gender, Age, City
    )
    c1.execute(q)
    con.commit()
    print("Patient details added successfully")


def showPatient():
    print("\n SHOWING ALL PATIENT DETAILS")
    c1 = con.cursor()
    c1.execute("SELECT * FROM PATIENT1")
    rec = c1.fetchall()
    print("S.No  Pt_Code  Pt_Name  Health_Issue  Gender  Age  City")
    for i in rec:
        print(i)


def delPatient():
    print("\n DELETING PATIENT DETAILS")
    pcode = input("Enter Patient Code to delete: ")
    c1 = con.cursor()
    q = "DELETE FROM PATIENT1 WHERE Pt_Code='{}'".format(pcode)
    c1.execute(q)
    con.commit()
    print("Patient record deleted successfully")


def apptStatus():
    print("\n SHOWING APPOINTMENT STATUS")
    apt = input("Enter Patient Code: ")
    c1 = con.cursor()
    q = "SELECT Pt_Code, Appt_Status FROM APPOINTMENT2 WHERE Pt_Code='{}'".format(apt)
    c1.execute(q)
    rec = c1.fetchall()
    for r in rec:
        print(r)


def apptDate():
    print("\n SHOWING APPOINTMENT DATE")
    apt = input("Enter Patient Code: ")
    c1 = con.cursor()
    q = "SELECT Pt_Code, Appt_Date FROM APPOINTMENT2 WHERE Pt_Code='{}'".format(apt)
    c1.execute(q)
    rec = c1.fetchall()
    for r in rec:
        print(r)



connect()
print("Connected to HEALTHCARE Database")

while True:
    print("\n ----------HEALTHCARE MANAGEMENT-----------")
    print("1 - Add a New Doctor")
    print("2 - Show details of all Doctors")
    print("3 - Delete Doctor record")
    print("4 - Add a New Patient")
    print("5 - Show all Patient records")
    print("6 - Delete Patient record")
    print("7 - Show Appointment Status")
    print("8 - Show Appointment Date")
    print("9 - EXIT")

    ch = int(input("Enter Your Choice : "))

    if ch == 1:
        addDoctor()
    elif ch == 2:
        showDoctors()
    elif ch == 3:
        delDoctor()
    elif ch == 4:
        addPatient()
    elif ch == 5:
        showPatient()
    elif ch == 6:
        delPatient()
    elif ch == 7:
        apptStatus()
    elif ch == 8:
        apptDate()
    elif ch == 9:
        print("EXITING..... Thank You!")
        break
    else:
        print("Invalid choice! Please try again.")
