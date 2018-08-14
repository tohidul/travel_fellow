import  sqlite3
conn = sqlite3.connect("travel_fellow.db")
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS travelData(Travel_ID INTEGER PRIMARY KEY, Place_Name TEXT, Distance_Type TEXT, Budget TEXT, Day TEXT, Security REAL, Season Text, Season_Type TEXT, Location_Heuristic REAL, Loc_Flag REAL, Hotel_Name TEXT, Distance_From_Spot TEXT, Comfortness TEXT, Hotel_Rent TEXT, Rating REAL, People REAL, Hotel_Heuristic REAL)')
