from connectfilm import *



def title(): # option 1
    titleField = input("Enter the name of the film Title to search for:  ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title = '{titleField}' ")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)

def yearReleased():  # option 2
    yearReleasedField = input("Enter the film of yearReleased to search for:  ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Artist = '{yearReleasedField}' ")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)

def rating(): # option 3
    ratingField = input("Enter the name of the film rating to search for:  ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title = '{ratingField}' ")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)

def duration(): # option 4
    durationField = input("Enter the name of the film duration to search for:  ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title = '{durationField}' ")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



def genre(): # option 5
    genreField = input("Enter the name of the film Genre to search for:  ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Genre = '{genreField}' ")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)


def filmID(): # option 6
    idField = input("Enter the filmID of the record to search to be deleted: ")
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField} ")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



# fieldName = input("Enter Field Name: ")

def readOrder(): # option 7
    # dbCursor.execute(f"SELECT * FROM tblFilms ORDER BY {fieldName} DESC")
    # dbCursor.execute(f"SELECT * FROM tblFilms ORDER BY filmID DESC")
    # dbCursor.execute(f"SELECT title, Genre FROM tblFilms ORDER BY filmID DESC")
    dbCursor.execute(f"SELECT title, Genre FROM tblFilms ORDER BY title ASC")
    # dbCursor.execute(f"SELECT * FROM tblFilms WHERE Genre = 'action' or Genre = 'drama' ")
    # dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title Like 'b%' ")
    # dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title Like '%b%' ")
    # dbCursor.execute(f"SELECT * FROM tblFilms WHERE Title NOT Like 'b%' ")
       
    #  https://www.w3schools.com/mysql/mysql_like.asp

    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)



if __name__=="__main__":
    # title()
    # yearReleased()
    # rating()
    # during()
    # genre()
    # filmID()
    readOrder()
  