import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QHBoxLayout, QDialog, QCalendarWidget)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.button2 = QPushButton("Clear")
        self.calender = QCalendarWidget()
        # Create layout and add widgets
        #
        layout = QVBoxLayout()
        layout.addWidget(self.edit)


        #layout.addWidget(self.button2)
        #
        layout2 = QVBoxLayout()
        layout2.addWidget(self.button)
        layout2.addWidget(self.button2)
        layout2.insertStretch(1)
        layout2.insertStretch(2)
        #
        #
        layout3 = QHBoxLayout()
        layout3.addLayout(layout)
        layout3.addLayout(layout2)

        # Set dialog layout
        self.setLayout(layout3)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)
        self.button2.clicked.connect(self.cleartext)

    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())

    # Clear all text
    def cleartext(self):
        self.edit.clear()

    def setdate(self):
        self.edit.insert(str(self.calender.dateTextFormat()))

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

