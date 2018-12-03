import mysql.connector

# Execute:
# python3 fifa18.py
# user is able to create a new addition to table called clubs

def insertClub():


    lastid = input("Id :")
    name = input("Club Name: ")
    clubcity = input("City: ")
    budget = input("Budget: ")


    mycursor = mydb.cursor()

    sql = "INSERT INTO clubs (clubID, club_name, club_city, club_budget) " \
                                   "VALUES(%s,%s,%s,%s)"
  
    arg = (lastid, name, clubcity, budget )

    mycursor.execute(sql, arg)
    
    mydb.commit()
    print(mycursor.rowcount, "record(s) added")

def insertPlayer():
   
    playerID = input("Id: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    birth = input("Birthday(yy-mm-dd): ")
    salary = input("Salary: ")
    worth = input("Net Worth: ")
        
    mycursor = mydb.cursor()
    
    sql = "insert into players (playerID, play_fname, play_lname, play_born, play_salary, play_networth) "\
                "value (%s,%s,%s,%s,%s,%s)"
    arg = (playerID, fname, lname, birth, salary, worth )
    mycursor.execute(sql, arg)
    
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) added")

#def insertAttributes():
    
#def insertClubMembers():
    
    
    
    
def showAllMembers():

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM club_members")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
    
    return;

def findByClub(): 
    
    club = input("Club: ")

    mycursor = mydb.cursor()

    sql = "SELECT firstname, lastname, club_name " \
          "FROM club_members join clubs " \
          "ON club_members.clubID = clubs.clubID " \
          "WHERE club_name = %s"
    
    arg = (club, )

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
    
    return;


def findAttributesByLastName():

    name = input("Player Last Name: ")

    mycursor = mydb.cursor()

    sql = "SELECT players.playerID, attr_agility, attr_crossing, attr_balance, attr_specialty " \
          "FROM attributes join players " \
          "ON attributes.playerID = players.playerID "\
          "WHERE play_lname = %s"

    arg = (name, )

    mycursor.execute(sql, arg)

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
    
    return;

def deletePlayer():
    
    lname = input("Last Name: ")
    
    mycursor = mydb.cursor()

    sql = "DELETE FROM players WHERE play_lname = %s"
        
    arg = (lname,)
    
    mycursor.execute(sql, arg)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
    
    return;

def updateSalary():
    
    mycursor = mydb.cursor()
    
    lname = input("Last Name: ")
    newSal = input("New Salary: ")

    sql = "UPDATE players SET play_salary = %s WHERE play_lname = %s"
   
    arg = (newSal, lname,)

    mycursor.execute(sql, arg)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")
    
    return;
  


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="fifa"
)

option = 0;

while option != 8: 
    
    print("")
    print("1. Add a club.")
    print("2. Add a palyer.")
    print("3. Show all club members.")
    print("4. Find player by club.")
    print("5. Retrieve player attributes.")
    print("6. Update player salary.")
    print("7. Delete player.")
    print("8. Exit")
    
    option = int(input("Choice: "))
    print (option)
    if option == 1:
        insertClub()
    elif option == 2:
        insertPlayer()
    elif option == 3:
        showAllMembers()
    elif option == 4:
        findByClub()
    elif option == 5:
        findAttributesByLastName()
    elif option == 6:
        updateSalary()
    elif option == 7:
        deletePlayer()
    else:
        print("You have exited the program.")
      
        