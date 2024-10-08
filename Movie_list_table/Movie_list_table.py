
from tkinter import *
import pyodbc

# back end

def showBtn():
    db_file = r'"U:\Lvl 4 IT\JOHAN\4dca\Movie_list_table.accdb"'

    # Establish a connection to the database
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
    conn = pyodbc.connect(conn_str)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    sqlComm = 'SELECT * FROM People;'

    try:
        # Execute a SELECT query
        cursor.execute(sqlComm)  # Replace YourTableName with your table name

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print column headers
        columns = [column[0] for column in cursor.description]
        print('\t'.join(columns))

        # Print each row
        for row in rows:
            print('\t'.join(str(item) for item in row))

    except pyodbc.Error as e:
        print(f"Error accessing database: {e}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()


# front end

widget = Tk() # creates the widget object from tkinter

widget.title("2018000485 Movie_list")
widget.geometry("400x200")

# creating labels and textboxes

titleLabel = Label(widget, text="Title")
MratingLabel = Label(widget, text="Maturity rating")
RdateLabel = Label(widget, text="Release date")
reviewLabel = Label(widget, text="Review")

titleTxtbx = Entry(widget, width=10)
MratingTxtbx = Entry(widget, width=10)
RdateTxtbx = Entry(widget, width=10)
reviewTxtbx = Entry(widget, width=10)

# first column elements
titleLabel.grid(row=1, column=1)
RdateLabel.grid(row=4, column=1)

# 2nd column elements
titleTxtbx.grid(row=1, column=2, padx=10, pady=5)
RdateTxtbx.grid(row=4, column=2, padx=10, pady=5)

# 3rd column elements
MratingLabel.grid(row=1, column=3, padx=10, pady=5)
reviewLabel.grid(row=4, column=3, padx=10, pady=5)

# 4th column elements
MratingTxtbx.grid(row=1, column=4, padx=10, pady=5)
reviewTxtbx.grid(row=4, column=4, padx=10, pady=5)

# create buttons

submitBtn = Button(widget, text="Submit").grid(row=7, column=2, padx = 10, pady=5)
showBtn = Button(widget, text="Show all", command=showBtn).grid(row=7, column=3, padx = 10, pady=5)
quitBtn = Button(widget, text="Quit").grid(row=7, column=4, padx = 10, pady=5)

widget.mainloop() # runs mainloop to show widget

from tkinter import *
import pyodbc

# back end

def showBtn():
    db_file = r'"U:\Lvl 4 IT\JOHAN\4dca\Movie_list_table.accdb"'

    # Establish a connection to the database
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
    conn = pyodbc.connect(conn_str)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    sqlComm = 'SELECT * FROM Movie_listTbl;'

    try:
        # Execute a SELECT query
        cursor.execute(sqlComm)  # Replace YourTableName with your table name

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Print column headers
        # columns = [column[0] for column in cursor.description]
        # print('\t'.join(columns))

        print(f'{"Title":<70}{"Maturity rating":<20}{"Release date":<20}{"Review":<20}')

        # Print each row
        for row in rows:
            # print('\t'.join(str(item) for item in row))

            relDate = row.Release_date.strftime("%d-%m-%Y")

            List_movie = f'{row.Title:<70}{row.Maturity_rating:<20}{relDate:<20}{row.Review:<20}'
            print(List_movie)
            
    except pyodbc.Error as e:
        print(f"Error accessing database: {e}")

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()
        
# def submitBtn():
#     db_file = r'"U:\Lvl 4 IT\JOHAN\4dca\Movie_list_table.accdb"'

#     # Establish a connection to the database
#     conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
#     conn = pyodbc.connect(conn_str)

#     # Create a cursor object to interact with the database
#     cursor = conn.cursor()
    
#     sqlComm = f'INSERT INTO People VALUES (51, "Johan", "Ong", "johan@gmail.com";'

#     cursor.execute(sqlComm)
    
#     conn.commit()
    
#     cursor.close()
#     conn.close()
# front end

widget = Tk() # creates the widget object from tkinter

widget.title("Assessment 2")
widget.geometry("400x200")

# creating labels and textboxes

titleLabel = Label(widget, text="Title")
MratingLabel = Label(widget, text="Maturity rating")
RdateLabel = Label(widget, text="Release date")
reviewLabel = Label(widget, text="Review")

titleTxtbx = Entry(widget, width=10)
MratingTxtbx = Entry(widget, width=10)
RdateTxtbx = Entry(widget, width=10)
reviewTxtbx = Entry(widget, width=10)

# first column elements
titleLabel.grid(row=1, column=1)
RdateLabel.grid(row=4, column=1)

# 2nd column elements
titleTxtbx.grid(row=1, column=2, padx=10, pady=5)
RdateTxtbx.grid(row=4, column=2, padx=10, pady=5)

# 3rd column elements
MratingLabel.grid(row=1, column=3, padx=10, pady=5)
reviewLabel.grid(row=4, column=3, padx=10, pady=5)

# 4th column elements
MratingTxtbx.grid(row=1, column=4, padx=10, pady=5)
reviewTxtbx.grid(row=4, column=4, padx=10, pady=5)

# create buttons

submitBtn = Button(widget, text="Submit").grid(row=7, column=2, padx = 10, pady=5)
showBtn = Button(widget, text="Show all", command=showBtn).grid(row=7, column=3, padx = 10, pady=5)
quitBtn = Button(widget, text="Quit").grid(row=7, column=4, padx = 10, pady=5)

widget.mainloop() # runs mainloop to show widget

def submitBtn():
    # get data from text box
    Title = titleTxtbx.get()
    Maturity = MratingTxtbx.get()
    Rel_date = RdateTxtbx.get()
    Review = reviewTxtbx.get()
    
    db_file = r'"U:\Lvl 4 IT\JOHAN\4dca\Movie_list_table.accdb"'

    # Establish a connection to the database
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file
    conn = pyodbc.connect(conn_str)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    
   

    cursor.execute("INSERT INTO Movie_listTbl (Title, Maturity_rating, Release_date, Review) VALUES (?, ?, ?, ?);",(Title, Maturity, Rel_date, Review))
    
    
    conn.commit()
    
    cursor.close()
    conn.close()