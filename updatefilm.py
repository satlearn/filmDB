from connectfilm import *
import readfilm
import time

#subroutine/function
def update():
    #use primary key to update a record
    idField = input("Enter the filmID of the record to be updated: ")

    #field to be updated: Title, yearReleased, rating, Genre
    fieldName = input("Enter Title or yearReleased or rating or Genre as field name: ").title()

    # fieldValue: ask for the value for the field to be updated
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    # print(fieldValue)

    # add single quote on either side of string
    fieldValue = "'" + fieldValue + "'" 
    # print(fieldValue)

    # update a record in tblFilms table
    " UPDATE films SET {Title or yearReleased or rating or Genre} = {fieldValue for Title or yearReleased or rating or Genre} WHERE filmID ={1/2/3/4..}                "
    dbCursor.execute(F"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField} ")
    dbCon.commit()# save changes to the db table permanently
    print(f"Record {idField}: {fieldValue} updated in the tblFilms table")

    # read from db
    # call/invoke the sleep method from the time module 
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readfilm module
    readfilm.read()

if __name__=="__main__":
    update()