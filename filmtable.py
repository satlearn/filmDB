from connectfilm import * # import the connectfilm.py module 
dbCursor.execute(""" 
CREATE TABLE "members" (
	"MemberID"	INTEGER NOT NULL UNIQUE,
	"Firstname"	TEXT,
	"Lastname"	TEXT,
	"Email"	TEXT,
	PRIMARY KEY("MemberID" AUTOINCREMENT)
)""")

# ...............................
dbCursor.execute("""
CREATE TABLE "tblFilms" (
	"filmID"	INTEGER NOT NULL UNIQUE,
	"title" TEXT 
    "yearReleased"
	"rating"	TEXT,
	"duration"	TEXT,
	"Genre"	TEXT,
	PRIMARY KEY("filmID" AUTOINCREMENT)
)""")
# ......... Create the table(s) with the foreigh keys last..................
dbCursor.execute("""
  CREATE TABLE "downloads" (
	"DownlID"	INTEGER NOT NULL UNIQUE,
	"filmID"	INTEGER,
	"MemberID"	INTEGER,
	"Date"	TEXT,
	PRIMARY KEY("DownlID" AUTOINCREMENT),
	FOREIGN KEY("filmID") REFERENCES "tblFilms"("SongID"),
	FOREIGN KEY("MemberID") REFERENCES "members"("MemberID")
)""")
