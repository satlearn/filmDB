from connectfilm import * # import the connectfilm.py module 



#subroutine/function

def read():
    dbCursor.execute("SELECT * FROM tblFilms")# select all records from tblFilms table
    records = dbCursor.fetchall()# fetches all records selected from the tblFilms table
    for aRecord in records: # loop though all the records held in the records variable
        print(aRecord)
if __name__=="__main__":
    read()


