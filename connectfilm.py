import sqlite3 as sql # import the sqlite3 module

dbCon = sql.connect("pyhton_project/filmflix.db")


dbCursor = dbCon.cursor()
