from connectfilm import *  # Import the connect.py module
import readfilm
import time  # Import the time module

# Subroutine/function
def insertfilms():
    # Ask for user input
    title = input("Enter film Title: ")
    yearReleased = input("Enter film Releasing year: ")
    rating = input("Enter film rating: ")
    duration = input("Enter duration: ")
    genre = input("Enter film genre: ")

    # Create a tuple with the user input values
    film_data = (title, yearReleased, rating, duration, genre)

    # Insert data saved in the tuple (film_data) into the tblFilms table
    dbCursor.execute("INSERT INTO tblFilms(Title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)", film_data)
    dbCon.commit()  # Save the changes to the database table permanently

    print(f"{title} inserted into the tbFfilms")

    # Call/invoke the sleep method from the time module
    time.sleep(3)  # Delay execution(code block below) for a given number of seconds

    # Call/invoke the read subroutine/function from the readfilm module
    readfilm.read()

if __name__ == "__main__":
    insertfilms()
