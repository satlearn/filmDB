import connectfilm
import readfilm
import time

#subroutine/function
def delete():
     #use primary key to delete a record
    idField = input("Enter the filmID of the record to be deleted: ")

    "DELETE FROM songs WHERE filmID = 1/2/3/4/5/......"
    connectfilm.dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    connectfilm.dbCon.commit()

    print(f"Record {idField} deleted from the tblFilms table")

    # read from db
    # call/invoke the sleep method from the time module 
    time.sleep(3) # Delay execution(code block below) for a given number of seconds

    # call/invoke the read subroutine/function from the readfilm module
    readfilm.read()


if __name__=="__main__":
    delete()




    