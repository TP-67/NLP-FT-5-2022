'''
Adapt from: https://www.geeksforgeeks.org/pyqt5-rock-paper-and-scissor-game/
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # User's choice
        self.choice = 0

        # Set the title
        self.setWindowTitle('Python Games')

        # Set window's geometry
        self.setGeometry(600, 300, 320, 400)

        # Set GUI components
        self.gui_components()

        # Plot everything
        self.show()

    # GUI components
    def gui_components(self):

        # Create a head label
        head = QLabel('Rock . Paper . Scissor', self)

        # Set geometry of the head
        head.setGeometry(20, 10, 280, 60)

        # Set font of the head
        font = QFont('Times', 15)
        font.setBold(True)
        font.setItalic(True)
        head.setFont(font)

        # Set alignment of the head
        head.setAlignment(Qt.AlignCenter)

        # Set color effect of the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)

        # Create a VS label
        self.vs = QLabel('vs', self)

        # Set geometry of the VS
        self.vs.setGeometry(150, 110, 30, 50)

        # Set font of the vS
        font.setUnderline(False)
        font.setItalic(False)
        self.vs.setFont(font)

        # Create a user choice label
        self.user = QLabel('You', self)

        # Set geometry of the user choice label
        self.user.setGeometry(50, 100, 70, 70)
        self.user.setStyleSheet('border : 2px solid black; background : white;')

        # Set alignment of the user choice label
        self.user.setAlignment(Qt.AlignCenter)

        # Create a computer choice label
        self.computer = QLabel('Computer', self)

        # Set geometry of the computer choice label
        self.computer.setGeometry(200, 100, 70, 70)
        self.computer.setStyleSheet('border : 2px solid black; background : white;')

        # Set alignment of the computer choice label
        self.computer.setAlignment(Qt.AlignCenter)

        # Create a result label
        self.result = QLabel(self)

        # Set geometry of the result label
        self.result.setGeometry(25, 200, 270, 50)

        # Set font of the result label
        self.result.setFont(QFont('Times', 14))

        # Set alignment of the result label
        self.result.setAlignment(Qt.AlignCenter)

        # Set border and color of the result label
        self.result.setStyleSheet('border : 2px solid black; background : white;')

        # Create three push button for rock paper and scissor
        self.rock = QPushButton('Rock', self)
        self.rock.setGeometry(30, 270, 80, 35)

        self.paper = QPushButton('Paper', self)
        self.paper.setGeometry(120, 270, 80, 35)

        self.scissor = QPushButton('Scissor', self)
        self.scissor.setGeometry(210, 270, 80, 35)

        # Add actions to all the buttons
        self.rock.clicked.connect(self.rock_action)
        self.paper.clicked.connect(self.paper_action)
        self.scissor.clicked.connect(self.scissor_action)

        # Create a push button to reset games
        game_reset = QPushButton('Reset', self)

        # Set geometry of the reset button
        game_reset.setGeometry(100, 320, 120, 50)

        # Set color effect of the reset button
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.red)
        game_reset.setGraphicsEffect(color)

        # Add an action to the reset button
        game_reset.clicked.connect(self.reset_action)

    def show_time(self):
        self.comp_choice = random.randint(1, 3)

        if self.comp_choice == 1:
            # Set the rock image to the computer label
            self.computer.setStyleSheet('border-image : url(imgs/rock.png);')
        elif self.comp_choice == 2:
            # Set the paper image to the computer label
            self.computer.setStyleSheet('border-image : url(imgs/paper.png);')
        else:
            # Set the scissor image to the computer label
            self.computer.setStyleSheet('border-image : url(imgs/scissor.png);')

        # Check the winner
        self.who_won()

    def rock_action(self):
        self.choice = 1

        # Set the rock image to the user label
        self.user.setStyleSheet('border-image : url(imgs/rock.png);')

        # Disable the push button
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)

        # Computer's turn
        self.show_time()

    def paper_action(self):
        self.choice = 2

        # Set the paper image to the user label
        self.user.setStyleSheet('border-image : url(imgs/paper.png);')

        # Disable the push button
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)

        # Computer's turn
        self.show_time()

    def scissor_action(self):
        self.choice = 3

        # Set the scissor image to the user label
        self.user.setStyleSheet('border-image : url(imgs/scissor.png);')

        # Disable the push button
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)

        # Computer's turn
        self.show_time()

    def reset_action(self):
        # Initialization
        self.result.setText('')
        self.user.setText('You')
        self.computer.setText('Computer')

        # Enable the push buttons
        self.rock.setEnabled(True)
        self.paper.setEnabled(True)
        self.scissor.setEnabled(True)

        # Remove images from the user and computer labels
        self.user.setStyleSheet('border-image : null;')
        self.computer.setStyleSheet('border-image : null;')

        self.user.setGeometry(50, 100, 70, 70)
        self.user.setStyleSheet('border : 2px solid black; background : white;')

        self.computer.setGeometry(200, 100, 70, 70)
        self.computer.setStyleSheet('border : 2px solid black; background : white;')

    def who_won(self):
        # Initialization
        self.computer.setText('')
        self.user.setText('')

        # If a match is draw
        if self.choice == self.comp_choice:
            self.result.setText('Draw Match')
        else:
            # User choose rock
            if self.choice == 1:
                # Computer choose paper
                if self.comp_choice == 2:
                    self.result.setText('Computer Wins')
                else:
                    self.result.setText('User Wins')
            # User chooses paper
            elif self.choice == 2:
                # Computer choose scissor
                if self.comp_choice == 3:
                    self.result.setText('Computer Wins')
                else:
                    self.result.setText('User Wins')
            # User chooses scissor
            elif self.choice == 3:
                # Computer choose rock
                if self.comp_choice == 1:
                    self.result.setText('Computer Wins')
                else:
                    self.result.setText('User Wins')


# Create pyqt5 app
App = QApplication(sys.argv)

# Create an instance of the Window
window = Window()

# Start the app
sys.exit(App.exec())
