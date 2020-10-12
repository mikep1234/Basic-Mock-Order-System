from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QIcon
import sqlite3
import tkinter

qss_file = open('STYLES/STYLES.qss').read()

FILE = sqlite3.connect("PYTHON FILES/CREDENTIALS.db")

CURSOR = FILE.cursor()

CURSOR.execute('CREATE TABLE IF NOT EXISTS Credentials(Username TEXT, Password TEXT)')

sentinel = 0

class MAIN_WINDOW(QMainWindow):

    def __init__(self):

        self.SCREEN_X = tkinter.Tk().winfo_screenwidth()
        self.SCREEN_Y = tkinter.Tk().winfo_screenheight()

        super().__init__()

        self.setWindowTitle("Order Entry")
        self.ICON = QIcon("STYLES/WINDOW_ICON_SHOPPING_CART.png")
        self.setWindowIcon(self.ICON)

        self.setGeometry(0, 0, self.SCREEN_X, self.SCREEN_Y)
        self.setStyleSheet(qss_file)

        self.show()

        self.Active_Widgets = []

        self.ORDERS = CURSOR.execute('SELECT * FROM Orders').fetchall()[-1][-1]

        self.BOOT_SCREEN()

    def paintEvent(self, paintEvent):

        self.DRAWING_TOOL = QPainter(self)
        self.DRAWING_TOOL.setBrush(QColor(147, 22, 33))
        self.DRAWING_TOOL.begin(self)
        self.DRAWING_TOOL.drawRect(0, 0, 300, self.SCREEN_Y)
        self.DRAWING_TOOL.drawRect(self.SCREEN_X - 300, 0, self.SCREEN_X, self.SCREEN_Y)
        self.DRAWING_TOOL.end()

    def BOOT_SCREEN(self):

        self.Remove_Widgets()

        self.Username = QLineEdit(self)
        self.Password = QLineEdit(self)

        self.Username_Label = QLabel(self)
        self.Password_Label = QLabel(self)

        self.Password_Label.setText("Password: ")
        self.Username_Label.setText("Username: ")

        self.Active_Widgets.append(self.Username)
        self.Active_Widgets.append(self.Password)

        self.Active_Widgets.append(self.Password_Label)
        self.Active_Widgets.append(self.Username_Label)

        self.Username.setGeometry(int(self.SCREEN_X / 2 - 150), int(self.SCREEN_Y / 2), 300, 30)
        self.Password.setGeometry(int(self.SCREEN_X / 2 - 150), int(self.SCREEN_Y / 2 + 40), 300, 30)

        self.Username_Label.setGeometry(int(self.SCREEN_X / 2 - 280), int(self.SCREEN_Y / 2), 140, 30)
        self.Password_Label.setGeometry(int(self.SCREEN_X / 2 - 280), int(self.SCREEN_Y / 2 + 40), 140, 30)

        self.Password.setEchoMode(QLineEdit.Password)

        self.BUTTON = QPushButton("Sign in", self)

        self.Active_Widgets.append(self.BUTTON)

        self.BUTTON.setGeometry(int(self.SCREEN_X / 2 - 50), int(self.SCREEN_Y / 2 + 80), 100, 40)

        self.BUTTON.clicked.connect(self.Sign_In)

        for elem in self.Active_Widgets:
            elem.setStyleSheet(qss_file)
            elem.show()

    def Order_Entry(self):

        self.Remove_Widgets()

        global sentinel
        sentinel += 1

        self.CLIENT_NAME_LABEL = QLabel(self)
        self.CLIENT_ADDRESS_LABEL = QLabel(self)
        self.CLIENT_EMAIL_LABEL = QLabel(self)
        self.PRODUCT_NAME_LABEL = QLabel(self)
        self.AMOUNT_LABEL = QLabel(self)
        self.SEARCH_DISPLAY = QTextEdit(self)

        self.CLIENT_NAME_LABEL.setText("Client name: ")
        self.CLIENT_ADDRESS_LABEL.setText("Client address: ")
        self.CLIENT_EMAIL_LABEL.setText("Email: ")
        self.PRODUCT_NAME_LABEL.setText("Product name: ")
        self.AMOUNT_LABEL.setText("Amount: ")
        self.SEARCH_DISPLAY.setReadOnly(True)

        self.CLIENT_NAME_LABEL.setGeometry(int(self.SCREEN_X / 2 - 450), int(self.SCREEN_Y / 2 - 300), 300, 30)
        self.CLIENT_ADDRESS_LABEL.setGeometry(int(self.SCREEN_X / 2 - 450), int(self.SCREEN_Y / 2 -225), 300, 30)
        self.CLIENT_EMAIL_LABEL.setGeometry(int(self.SCREEN_X / 2 - 450), int(self.SCREEN_Y / 2 -145), 300, 30)
        self.PRODUCT_NAME_LABEL.setGeometry(int(self.SCREEN_X / 2 - 450), int(self.SCREEN_Y / 2 -65), 300, 30)
        self.AMOUNT_LABEL.setGeometry(int(self.SCREEN_X / 2 - 450), int(self.SCREEN_Y / 2 + 15), 300, 30)
        self.SEARCH_DISPLAY.setGeometry(int(self.SCREEN_X / 2 + 70), int(self.SCREEN_Y / 2 - 225), 400, 300)

        self.CLIENT_NAME = QLineEdit(self)
        self.CLIENT_ADDRESS = QLineEdit(self)
        self.CLIENT_EMAIL = QLineEdit(self)
        self.PRODUCT_NAME = QLineEdit(self)
        self.AMOUNT = QLineEdit(self)
        self.SEARCH_BAR = QLineEdit(self)

        self.SUBMIT = QPushButton("Submit Client's \n Order Now", self)
        self.ENTER_SEARCH = QPushButton("Search", self)
        self.HELP_BUTTON = QPushButton("About and \n Void", self)
        self.SIGN_OUT = QPushButton("Sign \n out", self)

        self.CLIENT_NAME.setGeometry(int(self.SCREEN_X / 2 - 270), int(self.SCREEN_Y / 2 - 300), 300, 30)
        self.CLIENT_ADDRESS.setGeometry(int(self.SCREEN_X / 2 - 270), int(self.SCREEN_Y / 2 -225), 300, 30)
        self.CLIENT_EMAIL.setGeometry(int(self.SCREEN_X / 2 - 270), int(self.SCREEN_Y / 2 - 145), 300, 30)
        self.PRODUCT_NAME.setGeometry(int(self.SCREEN_X / 2 - 270), int(self.SCREEN_Y / 2 - 65), 300, 30)
        self.AMOUNT.setGeometry(int(self.SCREEN_X / 2 - 270), int(self.SCREEN_Y / 2 + 15), 300, 30)
        self.SEARCH_BAR.setGeometry(int(self.SCREEN_X / 2 + 70), int(self.SCREEN_Y / 2 - 300), 300, 30)

        self.SUBMIT.setGeometry(int(self.SCREEN_X / 2 - 450), int(self.SCREEN_Y / 2 + 60), 180, 60)
        self.SIGN_OUT.setGeometry(int(self.SCREEN_X / 2 - 260), int(self.SCREEN_Y / 2 + 60), 130, 60)
        self.HELP_BUTTON.setGeometry(int(self.SCREEN_X / 2 - 120), int(self.SCREEN_Y / 2 + 60), 180, 60)
        self.ENTER_SEARCH.setGeometry(int(self.SCREEN_X / 2 + 390), int(self.SCREEN_Y / 2 - 300), 100, 30)

        self.SUBMIT.clicked.connect(self.Add_Order)
        self.ENTER_SEARCH.clicked.connect(self.Order_Search)
        self.SIGN_OUT.clicked.connect(self.BOOT_SCREEN)
        self.HELP_BUTTON.clicked.connect(self.HELP_VOID)

        self.Active_Widgets.append(self.CLIENT_NAME)
        self.Active_Widgets.append(self.CLIENT_ADDRESS)
        self.Active_Widgets.append(self.AMOUNT)
        self.Active_Widgets.append(self.PRODUCT_NAME)
        self.Active_Widgets.append(self.CLIENT_EMAIL)
        self.Active_Widgets.append(self.SEARCH_BAR)

        self.Active_Widgets.append(self.CLIENT_NAME_LABEL)
        self.Active_Widgets.append(self.CLIENT_ADDRESS_LABEL)
        self.Active_Widgets.append(self.CLIENT_EMAIL_LABEL)
        self.Active_Widgets.append(self.AMOUNT_LABEL)
        self.Active_Widgets.append(self.PRODUCT_NAME_LABEL)
        self.Active_Widgets.append(self.SEARCH_DISPLAY)

        self.Active_Widgets.append(self.SUBMIT)
        self.Active_Widgets.append(self.ENTER_SEARCH)
        self.Active_Widgets.append(self.HELP_BUTTON)
        self.Active_Widgets.append(self.SIGN_OUT)

        for elem in self.Active_Widgets:
            elem.show()
            elem.setStyleSheet(qss_file)

    def HELP_VOID(self):

        self.Remove_Widgets()
        self.SUPPORT_TEXT = QTextEdit(self)
        self.SUPPORT_TEXT.setGeometry(350, 50, 900, 240)
        self.SUPPORT_TEXT.setReadOnly(True)
        self.HTML_FOR_HELP = open("STYLES/CONTACT_SHEET.html").read()
        self.SUPPORT_TEXT.setHtml(self.HTML_FOR_HELP)
        self.Active_Widgets.append(self.SUPPORT_TEXT)

        self.BACK = QPushButton("Back", self)
        self.Active_Widgets.append(self.BACK)
        self.BACK.setGeometry(350, 250, 100, 40)
        self.BACK.clicked.connect(self.Order_Entry)

        self.VOID_LABEL = QLabel(self)
        self.VOID_LABEL.setText("Void Order Number: ")
        self.VOID_LABEL.setGeometry(350, 300, 300, 40)
        self.Active_Widgets.append(self.VOID_LABEL)

        self.VOID_NUMBER = QLineEdit(self)
        self.VOID_NUMBER.setGeometry(600, 300, 300, 40)
        self.Active_Widgets.append(self.VOID_NUMBER)

        self.VOID_SUBMIT = QPushButton("Submit", self)
        self.VOID_SUBMIT.setGeometry(350, 350, 100, 40)
        self.VOID_SUBMIT.clicked.connect(self.add_voids)
        self.Active_Widgets.append(self.VOID_SUBMIT)

        for elem in self.Active_Widgets:
            elem.show()
            elem.setStyleSheet(qss_file)

    def add_voids(self):

        self.TEMP_ORDER_NUMBER = "\'" + self.VOID_NUMBER.text() + "\'"

        if self.TEMP_ORDER_NUMBER != "''" and self.TEMP_ORDER_NUMBER != "'0'":
            try:
                CURSOR.execute('DELETE FROM Orders WHERE order_number = ' + self.TEMP_ORDER_NUMBER)
            except:
                print("FAILED")
            FILE.commit()

            self.VOID_NUMBER.clear()

    def Order_Search(self):

        self.SEARCH_DISPLAY.clear()

        self.TEMP_NAME_SEARCH =  self.SEARCH_BAR.text()

        if len(self.TEMP_NAME_SEARCH) > 0:

            for elem in (CURSOR.execute('SELECT * FROM Orders')).fetchall():

                if elem != CURSOR.execute('SELECT * FROM Orders').fetchall()[0]:

                    if self.TEMP_NAME_SEARCH.lower() in str(elem[0]).lower():

                        self.SEARCH_DISPLAY.insertPlainText("Name: " + str(elem[0]) + "\n" + "Address: " + str(elem[1]) + "\n" + "Email: " + str(elem[2]) + "\n" + "Product Name: " + str(elem[3]) + "\n" + "Amount: " + str(elem[4]) + "\n" + "Order Number: " + str(elem[5]) + "\n" + "----------" + "\n")

        else:
            for elem in (CURSOR.execute('SELECT * FROM Orders').fetchall()):

                if elem != CURSOR.execute('SELECT * FROM Orders').fetchall()[0]:

                    self.SEARCH_DISPLAY.insertPlainText("Name: " + str(elem[0]) + "\n" + "Address: " + str(elem[1]) + "\n" + "Email: " + str(elem[2]) + "\n" + "Product Name: " + str(elem[3]) + "\n" + "Amount: " + str(elem[4]) + "\n" + "Order Number: " + str(elem[5]) + "\n" + "----------" + "\n")

    def Add_Order(self):

        self.ORDERS += 1
        self.TEMP_NAME = "\'" + self.CLIENT_NAME.text() + "\'"
        self.TEMP_EMAIL = "\'" + self.CLIENT_EMAIL.text() + "\'"
        self.TEMP_ADDR = "\'" + self.CLIENT_ADDRESS.text() + "\'"
        self.TEMP_PROD = "\'" + self.PRODUCT_NAME.text() + "\'"
        self.TEMP_AMOUNT = "\'" + self.AMOUNT.text() + "\'"

        if self.TEMP_EMAIL != "''" and self.TEMP_NAME != "''" and self.TEMP_ADDR != "''" and self.TEMP_PROD != "''" and self.TEMP_AMOUNT != "''":

            CURSOR.execute('INSERT INTO Orders VALUES(' + self.TEMP_NAME + ', ' + self.TEMP_ADDR + ', ' + self.TEMP_EMAIL + ', ' + self.TEMP_PROD + ', ' + self.TEMP_AMOUNT + ', ' + str(self.ORDERS) + ')')

            FILE.commit()

            self.CLIENT_ADDRESS.clear()
            self.PRODUCT_NAME.clear()
            self.CLIENT_EMAIL.clear()
            self.CLIENT_NAME.clear()
            self.AMOUNT.clear()

    def Sign_In(self):

        self.DATA = CURSOR.execute('SELECT * FROM Credentials')

        for elem in self.DATA.fetchall():

            if(elem[0] == self.Username.text()):

                if(elem[-1] == self.Password.text()):

                    self.Remove_Widgets()

                    self.Order_Entry()

    def Remove_Widgets(self):
        for item in self.Active_Widgets:

            item.hide()

        self.Active_Widgets = []

app = QApplication([])


window = MAIN_WINDOW()

app.exec_()