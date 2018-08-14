from Welcome_Window import Ui_Welcome_Window
from Make_Tour import Ui_MakeTour
from Find_Place import Ui_Find_Place
from Choose_Hotel import Ui_Choose_Hotel
from Hotel_Satisfaction import Ui_Hotel_Satisfaction
from Admin_Panel import Ui_AdminPanel
from PyQt4 import QtCore, QtGui
import sqlite3

place = ''
hotel = ''
#Display_Find Place
season = ''
budget = ''
distance_type = ''
day = ''
comfort = ''
#Display_Find place

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
class main_class(Ui_Welcome_Window, QtGui.QMainWindow):

    def warning_message(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setText('Select a hotel first')
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        msgBox.setFont(font)
        msgBox.setIcon(2)
        msgBox.setStyleSheet(_fromUtf8("background-color: rgb(170, 167, 80);;\n""color: rgb(0, 0, 255);"))
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def confirm_message(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle('Confirm')
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setText('Successfully Done')
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        msgBox.setFont(font)
        msgBox.setIcon(1)
        msgBox.setStyleSheet(_fromUtf8("background-color: rgb(170, 167, 80);;\n""color: rgb(0, 0, 255);"))
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def insert_database(self):
        loc_heuristic = 0.0
        hotel_heuristic = 0.0

        placename = self.ap.a_PlaceName.text()
        distance_type = self.ap.a_distance_type.currentText()
        budget = self.ap.a_budget.currentText()
        day = self.ap.a_duration.currentText()
        security = self.ap.a_hotel_security.currentText()
        season = self.ap.a_season.currentText()
        season_type = self.ap.a_on_off_season.currentText()
        loc_flag = 0

        hotel_name = self.ap.a_hotelname.text()
        distance_from_spot = self.ap.a_distance4spot.currentText()
        comfort = self.ap.a_comfortness.currentText()
        hotel_rent = self.ap.a_hotelrent.currentText()
        rate = 0.0
        people = 0.0

        ################    Database   #############

        conn = sqlite3.connect("travel_fellow.db")
        c = conn.cursor()


        if(budget == '<5000'):
            loc_heuristic += 40.0
        elif(budget == '5000 - 8000'):
            loc_heuristic += 30.0
        elif(budget == '8000 - 12000'):
            loc_heuristic += 20.0
        else:
            loc_heuristic += 10.0

        if(security == 'Satisfaction'):
            loc_heuristic += 10.0
        else:
            loc_heuristic += 15.0

        if(season_type == 'On Season'):
            loc_heuristic += 30.0
        else:
            loc_heuristic += 20.0

        ###########     hotel heuristic calculation

        if(distance_from_spot == 'Very Near'):
            hotel_heuristic += 40.0
        elif(distance_from_spot is 'Near'):
            hotel_heuristic += 30.0
        else:
            hotel_heuristic += 20.0

        if(hotel_rent == '<1000'):
            hotel_heuristic += 85.0
        elif(hotel_rent == '1000-2000'):
            hotel_heuristic += 70.0
        elif(hotel_rent == '2000-3000'):
            hotel_heuristic += 55.0
        else:
            hotel_heuristic += 40.0

        c.execute(
            "INSERT INTO travelData(Place_Name, Distance_Type, Budget, Day, Security, Season, Season_Type, Location_Heuristic, Loc_Flag, Hotel_Name, Distance_From_Spot, Comfortness, Hotel_Rent, Rating, People, Hotel_Heuristic)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
            placename, distance_type, budget, day, security, season, season_type, loc_heuristic, loc_flag,
            hotel_name, distance_from_spot, comfort, hotel_rent, rate, people, hotel_heuristic))
        conn.commit()
        c.close()
        conn.close()

        #garbege = QtGui.QMessageBox.information(self, 'Confirm', 'New Row Inserted', QtGui.QMessageBox.Yes)

        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle('Inform')
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setText('New Row Inserted')
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        msgBox.setFont(font)
        msgBox.setIcon(1)
        msgBox.setStyleSheet(_fromUtf8("background-color: rgb(170, 167, 80);\n""color: rgb(0, 0, 255);"))
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

        ################    Database   #############

    def display_admin_panel(self):
        if __name__ == "__main__":
            self.ap = Ui_AdminPanel()
            self.ap.setupUi(self.adminpanel_window)
            self.adminpanel_window.show()

            self.choosehotel_window.hide()
            self.maketour_window.hide()
            self.findplace_window.hide()
            self.hotelsatisfaction_window.hide()

            self.ap.a_addButton.clicked.connect(self.insert_database)
            self.ap.a_home.clicked.connect(self.display_make_tour)

    def rate_hotel(self):
        point = 0.0
        rating = 0.0
        flag = 0
        global hotel
        global place

        if (self.hs.extremely_satisfied.isChecked()):
            point = 3.0
            rating = 5.0
            flag = 1
        elif (self.hs.very_satisfied.isChecked()):
            point = 2.0
            rating = 4.0
            flag = 1
        elif (self.hs.satisfied.isChecked()):
            point = 1.0
            rating = 3.0
            flag = 1
        elif (self.hs.somewhat_satisfied.isChecked()):
            point = -2.0
            rating = 2.0
            flag = 1
        elif (self.hs.not_satisfied.isChecked()):
            point = -3.0
            rating = 1.0
            flag = 1
        ##########
        # Database for search hotel and update the rate value with people increase

        if(flag == 1):
            conn = sqlite3.connect("travel_fellow.db")
            c = conn.cursor()
            c.execute("SELECT Rating, People, Hotel_Heuristic, Travel_ID FROM travelData WHERE Hotel_Name = ? AND Place_Name = ?",
                      (hotel, place))
            for row in c.fetchall():
                t_rating = float(row[0])
                t_people = float(row[1])
                t_heuristic = float(row[2])
                t_id = row[3]

                t_rating = ((t_rating*t_people) + rating) / (t_people + 1)
                t_rating = round(t_rating, 2)
                t_people += 1
                t_heuristic += point

                c.execute("UPDATE travelData SET Rating = ? WHERE Travel_ID = ?",
                          (t_rating, t_id))
                c.execute("UPDATE travelData SET People = ? WHERE Travel_ID = ?",
                          (t_people, t_id))
                c.execute("UPDATE travelData SET Hotel_Heuristic = ? WHERE Travel_ID = ?",
                          (t_heuristic, t_id))

                self.confirm_message()
            conn.commit()
            c.close()
            conn.close()
            self.display_make_tour()

    def display_hotel_satisfaction(self):
        global hotel
        if __name__ == "__main__":
            self.hs = Ui_Hotel_Satisfaction()
            self.hs.setupUi(self.hotelsatisfaction_window)
            self.hotelsatisfaction_window.show()

            self.choosehotel_window.hide()
            self.maketour_window.hide()
            self.findplace_window.hide()
            self.adminpanel_window.hide()
            hotel = self.ch.search_hotel.text()

            self.hs.h_maketour.clicked.connect(self.display_make_tour)
            self.hs.h_findplace.clicked.connect(self.display_find_place)
            self.hs.h_choosehotel.clicked.connect(self.display_choose_hotel)
            self.hs.h_adminpanel.clicked.connect(self.display_admin_panel)
            self.hs.submit.clicked.connect(self.rate_hotel)

    def display_choose_hotel(self):

        global place
        global season
        global budget
        global distance_type
        global day
        global comfort
        #print(place, season, budget, distance_type, day, comfort)

        place = self.fp.search_place.text()
        if __name__ == "__main__":
            self.choosehotel_window = QtGui.QMainWindow()
            self.ch = Ui_Choose_Hotel()
            self.ch.setupUi(self.choosehotel_window)
            self.choosehotel_window.show()

            self.maketour_window.hide()
            self.findplace_window.hide()
            self.hotelsatisfaction_window.hide()
            self.adminpanel_window.hide()

            ################### search by place on database and then set text on box
            conn = sqlite3.connect("travel_fellow.db")
            c = conn.cursor()
            text = ''
            c.execute("SELECT DISTINCT Hotel_Name, Distance_From_Spot, Rating, Hotel_Rent from travelData WHERE Place_Name = ? AND Season = ? AND Budget = ? AND Distance_Type = ? AND Comfortness = ? ORDER BY Hotel_Heuristic DESC LIMIT 5",(place, season, budget, distance_type, comfort))
            for row in c.fetchall():
                text = text + row[0] + '\n\t'
                text = text + 'Distance from Spot: ' + row[1] + '\n\t' + 'Hotel Rate: ' + str(row[2]) + '\n\t'
                text = text + 'Hotel Rent per day: ' + row[3] + '\n\t' + '=====================================\n'

            c.execute("SELECT DISTINCT Hotel_Name, Distance_From_Spot, Rating, Hotel_Rent from travelData WHERE Place_Name = ? AND Season = ? AND Budget = ? AND Distance_Type = ? AND Comfortness = ? AND Rating = ? ORDER BY Hotel_Heuristic DESC LIMIT 1",(place, season, budget, distance_type, comfort, 0.0))
            for row in c.fetchall():
                text = text + '\n\nYou may also like this' + '\n'
                text = text + row[0] + '\n\t'
                text = text + 'Distance from Spot: ' + row[1] + '\n\t' + 'Hotel Rate: ' + str(row[2]) + '\n\t'
                text = text + 'Hotel Rent per day: ' + row[3] + '\n\t' + '====================================='

            self.ch.hotel_box.setText(text)

            c.close()
            conn.close()

            #####################    set priority for location heuristic
            conn = sqlite3.connect("travel_fellow.db")
            c = conn.cursor()
            c.execute("SELECT Travel_ID, Place_Name, Location_Heuristic from travelData WHERE Place_Name = ?", (place,))
            for row in c.fetchall():
                t_id = row[0]
                t_value = row[2]
                t_value -= 5
                l_flag = 1

                c.execute("UPDATE travelData SET Location_heuristic = ? WHERE Travel_ID = ?",
                          (t_value, t_id))
                c.execute("UPDATE travelData SET Loc_Flag = ? WHERE Travel_ID = ?",
                          (l_flag, t_id))

            conn.commit()
            c.close()
            conn.close()


            self.ch.c_maketour.clicked.connect(self.display_make_tour)
            self.ch.c_findplace.clicked.connect(self.display_find_place)
            self.ch.c_hotelsatisfaction.clicked.connect(self.display_hotel_satisfaction)
            self.ch.c_hotelsatisfaction_2.clicked.connect(self.display_hotel_satisfaction)
            self.ch.c_adminpanel.clicked.connect(self.display_admin_panel)

    def search_place(self):
        key = self.fp.f_search_box.text()
        text = ''
        conn = sqlite3.connect("travel_fellow.db")
        c = conn.cursor()
        c.execute("SELECT DISTINCT Place_Name, Distance_Type, Day, Season, Season_Type, Budget from travelData WHERE Place_Name LIKE ?", ('%'+key+'%',))
        for row in c.fetchall():
            text = text + row[0] + '\n\t'
            text = text + 'Distance: ' + row[1] + '\t' + 'Expected Day: ' + row[2] + '\n\t'
            text = text + row[3] + ' is ' + row[4]  + '\n\t'
            text = text + 'Approximate Budget: ' + row[5] + '\n\n' + '====================================='+'\n'

        conn.commit()
        c.close()
        conn.close()
        self.fp.place_box.setText(text)

    def display_find_place(self):
        global place
        global season
        global budget
        global comfort
        global distance_type
        global day

        if __name__ == "__main__":
            self.findplace_window = QtGui.QMainWindow()
            self.fp = Ui_Find_Place()
            self.fp.setupUi(self.findplace_window)
            self.findplace_window.show()

            self.maketour_window.hide()
            self.choosehotel_window.hide()
            self.hotelsatisfaction_window.hide()
            flag =0

            if (self.mt.check_summer.isChecked()):
                season = 'Summer'
                flag = 1
            elif (self.mt.check_winter.isChecked()):
                season = 'Winter'
                flag = 1
            elif (self.mt.check_spring.isChecked()):
                season = 'Spring'
                flag = 1

            if (self.mt.check_less_5k.isChecked()):
                budget = '<5000'
                flag = 1
            elif (self.mt.check_5k_8k.isChecked()):
                budget = '5000 - 8000'
                flag = 1
            elif (self.mt.check_8k_12k.isChecked()):
                budget = '8000 - 12000'
                flag = 1
            elif (self.mt.check_12k_plus.isChecked()):
                budget = '12000+'
                flag = 1

            distance_type = self.mt.m_distancetype.currentText()
            day = self.mt.m_tourduration.currentText()
            comfort = self.mt.m_comfortness.currentText()
            #print(place, season, budget, comfort, distance_type, day)
            #####################    Database    #################
            if(flag == 1):
                conn = sqlite3.connect("travel_fellow.db")
                c = conn.cursor()
                c.execute(
                    "SELECT DISTINCT Place_Name, Season, Season_Type, Security FROM travelData WHERE Season = ? AND Budget = ? AND Distance_Type = ? AND Day = ? AND Comfortness = ? ORDER BY Location_Heuristic DESC LIMIT 5",
                    (season, budget, distance_type, day, comfort))

                text = ''
                for row in c.fetchall():
                    text = text + row[0] + '\n\t'
                    text = text + row[1] + ' is ' + row[2] + '\n\t'
                    text = text + 'Security Level: ' + row[3] + '\n' + '=====================================' + '\n\n'

                c.execute("SELECT DISTINCT Place_Name, Season, Season_Type, Security FROM travelData WHERE Season = ? AND Budget = ? AND Distance_Type = ? AND Day = ? AND Comfortness = ? AND Loc_Flag = ? ORDER BY Location_Heuristic DESC LIMIT 1",
                          (season, budget, distance_type, day, comfort,0))

                for newrow in c.fetchall():
                    text = text + 'You may also like this' + '\n\n'
                    text = text + newrow[0] + '\n\t'
                    text = text + newrow[1] + ' is ' + newrow[2] + '\n\t'
                    text = text + 'Security Level: ' + newrow[3] + '\n'


                conn.commit()
                c.close()
                conn.close()
                self.fp.place_box.setText(text)

            self.fp.f_maketour.clicked.connect(self.display_make_tour)
            self.fp.f_choosehotel.clicked.connect(self.display_choose_hotel)
            self.fp.f_choosehotel_2.clicked.connect(self.display_choose_hotel)
            self.fp.f_adminpanel.clicked.connect(self.display_admin_panel)
            self.fp.f_search_button.clicked.connect(self.search_place)
            self.fp.f_hotelsatisfaction.clicked.connect(self.warning_message)


    def display_make_tour(self):
        if __name__ == "__main__":
            self.maketour_window = QtGui.QMainWindow()
            self.mt = Ui_MakeTour()
            self.mt.setupUi(self.maketour_window)
            self.maketour_window.show()

            self.hide()
            self.findplace_window.hide()
            self.choosehotel_window.hide()
            self.hotelsatisfaction_window.hide()
            self.adminpanel_window.hide()

            self.mt.m_findplace.clicked.connect(self.display_find_place)
            self.mt.m_choosehotel.clicked.connect(self.display_choose_hotel)
            self.mt.m_findplace_2.clicked.connect(self.display_find_place)
            self.mt.m_adminpanel.clicked.connect(self.display_admin_panel)
            self.mt.m_hotelsatisfaction.clicked.connect(self.warning_message)

    def __init__(self):
        super(main_class, self).__init__()
        self.setupUi(self)

        conn = sqlite3.connect("travel_fellow.db")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS travelData(Travel_ID INTEGER PRIMARY KEY, Place_Name TEXT, Distance_Type TEXT, Budget TEXT, Day TEXT, Security REAL, Season Text, Season_Type TEXT, Location_Heuristic REAL, Loc_Flag REAL, Hotel_Name TEXT, Distance_From_Spot TEXT, Comfortness TEXT, Hotel_Rent TEXT, Rating REAL, People REAL, Hotel_Heuristic REAL)')
        c.close()
        conn.close()

        self.maketour_window = QtGui.QMainWindow()
        self.mt = Ui_MakeTour()
        self.mt.setupUi(self.maketour_window)

        self.findplace_window = QtGui.QMainWindow()
        self.fp = Ui_Find_Place()
        self.fp.setupUi(self.findplace_window)

        self.choosehotel_window = QtGui.QMainWindow()
        self.ch = Ui_Choose_Hotel()
        self.ch.setupUi(self.choosehotel_window)


        self.hotelsatisfaction_window = QtGui.QMainWindow()
        self.adminpanel_window = QtGui.QMainWindow()

        self.start_button.clicked.connect(self.display_make_tour)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Welcome_Window = main_class()
    Welcome_Window.show()
    sys.exit(app.exec_())