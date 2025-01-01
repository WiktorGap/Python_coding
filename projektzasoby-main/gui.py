from PyQt5.QtWidgets import *
from connection_with_base import Connection
from main import variabilityBase
#nie wiem z czego wynika ale mam problem za zaimportowaniem main.py , connection_with_base i istancje z jego klas działają z kolei poprawinie zastanaiwam sie czy wynika to  nazewnicta czy błednie cos importuje??
app = QApplication([])
button = QPushButton('Click')
conection = Connection()
base = variabilityBase()
def on_button_clicked():
    #mam problem z połączniem, wyskakuje błąd z dekodowaniem, w connection_with.base.py mozna spróbowac dodac zmienna encodning i ustawic odpowidnia wartosc 
    #make connection 
    connect = conection.make_connection()
    if connect:
        cursor = conection.make_cursor()
        new_base = base.base_model()
        if new_base:
            # if connect was succesfull the table will be create 
            cursor.execute(new_base)
            connect.commit()
            connect.close()
        alert = QMessageBox()
        alert.setText('You are conneted with data base!')
        alert.exec()
    else:
       QMessageBox.warning(None, "Error", "Failed connection")


    

button.clicked.connect(on_button_clicked)
button.show()
app.exec()