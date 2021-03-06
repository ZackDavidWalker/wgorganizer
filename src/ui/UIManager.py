from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
from ui.UI_MainWindow import UI_MainWindow
from ui.UI_Cleaning import UI_Cleaning
from ui.UI_Members import UI_Members
from ui.UI_Settings import UI_Settings
from ui.UI_Dashboard import UI_Dashboard

class UIManager():
    def __init__(self):
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.mainWindow = QMainWindow()

        # Setup UI Widgets
        self.ui = UI_MainWindow()
        self.ui.setupUI(self.mainWindow)

        self.dashboardScreen = UI_Dashboard()
        self.ui.content.addWidget(self.dashboardScreen)

        self.cleaningScreen = UI_Cleaning()
        self.ui.content.addWidget(self.cleaningScreen)

        self.membersScreen = UI_Members()
        self.ui.content.addWidget(self.membersScreen)

        self.settingsScreen = UI_Settings()
        self.ui.content.addWidget(self.settingsScreen)

        self.switchTo("cleaning")

        self.ui.dashboardButton.clicked.connect(lambda: self.switchTo("dashboard"))
        self.ui.putzdienstButton.clicked.connect(lambda: self.switchTo("cleaning"))
        self.ui.membersButton.clicked.connect(lambda: self.switchTo("members"))
        self.ui.settingsButton.clicked.connect(lambda: self.switchTo("settings"))

    def switchTo(self, widgetName):
        if widgetName == "dashboard":
            self.ui.title.setText(self.dashboardScreen.title)
            self.ui.content.setCurrentWidget(self.dashboardScreen)
            self.currentScreen = self.dashboardScreen
        if widgetName == "cleaning":
            self.ui.title.setText(self.cleaningScreen.title)
            self.ui.content.setCurrentWidget(self.cleaningScreen)
            self.currentScreen = self.cleaningScreen
        elif widgetName == "members":
            self.ui.title.setText(self.membersScreen.title)
            self.ui.content.setCurrentWidget(self.membersScreen)
            self.currentScreen = self.membersScreen
        elif widgetName == "settings":
            self.ui.title.setText(self.settingsScreen.title)
            self.ui.content.setCurrentWidget(self.settingsScreen)
            self.currentScreen = self.settingsScreen

        self.currentScreen.onSwitch()

    def show(self):
        self.mainWindow.show()