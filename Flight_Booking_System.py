import mysql.connector

db =mysql.connector.connect(host='localhost',user='root',password='root' , database='flight')
my_cursor = db.cursor()


print("WELCOME TO FLIGHT BOOKING SYSTEM")

print("what do you want to do?")
print("1.see booked tickets")
print("2.book a ticket")

ans = int(input("Answer (1/2): "))
ticketView = ["Flight No: ", "Name of Passenger: ", "Destination: ", "Departure From: ", "Tickets Booked: "]
flightView = ["Flight No: ", "Destination: ", "Departure From: "]

if ans==1:
    num = input("ENTER FLIGHT NUMBER: ")
    query = "SELECT * FROM booked WHERE FLIGHT_NO =" + "'" + num + "'"
    my_cursor.execute(query)
    print("YOUR FLIGHT DATA IS---")
    for a in my_cursor:
        for i in range(len(a)):
            print(ticketView[i]+str(a[i]))


elif ans == 2:
    choice = input("Enter Destination: ")
    query = "SELECT * FROM flights WHERE DESTINATION LIKE" + "'%" + choice + "%'"
    my_cursor.execute(query)
    print("Flights available are :\n")
    for i in my_cursor:
        for j in range(len(i)):
            print(flightView[j] + i[j], end = "  ")
        print("\n")
    
    choice = input("Enter Flight No. you would like to travel with: ")
    name = input("Enter Name of Passenger: ")
    dest = ""
    dep = ""
    ticket = int(input("How Many tickets to book : "))
    my_cursor.execute("SELECT * FROM flights WHERE FLIGHT_NO ="+"'"+choice+"'")
    for i in my_cursor:
        for j in range(len(i)):
            if j == 1:
                dest = i[j]
            if j == 2:
                dep = i[j]

    query = "INSERT INTO BOOKED VALUE(%s,%s,%s,%s,%s)"
    val = (choice,name,dest,dep,ticket)
    my_cursor.execute(query,val)
    db.commit()
    print("Record Added Successfully. Happy Travels!")
    
