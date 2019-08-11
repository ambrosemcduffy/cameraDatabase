import json
import os
from qtpy import QtWidgets, QtGui, QtCore


class CameraLibraryUI(QtWidgets.QDialog):

    def __init__(self):
        super(CameraLibraryUI, self).__init__()
        self.data = self.loadData()
        self.setWindowTitle("Camera Libray UI")
        self.setFixedSize(510, 100)
        self.setWindowIcon(QtGui.QIcon("data/snip.png"))
        self.buildUI()

    def buildUI(self):
        '''
        This function builds the User Interface
        '''
        main_layout = QtWidgets.QVBoxLayout(self)
        camWidgetW = QtWidgets.QWidget()

        camLayout = QtWidgets.QHBoxLayout(camWidgetW)
        fbLayout = QtWidgets.QHBoxLayout(camWidgetW)

        main_layout.addWidget(camWidgetW)

        self.cameraField = QtWidgets.QComboBox()
        self.cameraField.addItems(sorted(self.data.keys()))
        self.cameraField.currentIndexChanged.connect(self.populateRes_Field)

        self.resField = QtWidgets.QComboBox()
        self.resField.currentIndexChanged.connect(self.populateTextField)
        self.resField.setFixedWidth(150)

        self.checkBoxField = QtWidgets.QCheckBox()
        self.label = QtWidgets.QLabel("Anamorphic")
        self.label.setFixedWidth(100)

        camLayout.addWidget(self.cameraField)
        camLayout.addWidget(self.resField)
        camLayout.addWidget(self.checkBoxField)
        camLayout.addWidget(self.label)

        self.fbField = QtWidgets.QLineEdit(self)
        self.fbField.setAlignment(QtCore.Qt.AlignCenter)
        self.fbField.move(24, 65)
        self.fbField.resize(110, 30)

        fbLayout.addWidget(self.fbField)

    def loadData(self):
        '''
        This function loads camera database
        from a json file
        and return a dictionary of the data
        '''
        if os.path.exists("data/data.json"):
            with open("data/data.json", "r") as f:
                data = json.load(f)
            return data
        else:
            print("data/data.json director does not exist")
            return None

    def populateRes_Field(self):
        '''
        This fuction populates the resolution field
        '''
        self.resField.clear()
        self.camName = self.cameraField.currentText()
        for res, _ in self.data[self.camName][0]:
            resolution = "{} x {}".format(res[0], res[1])
            self.resField.addItem(resolution)

    def populateTextField(self):
        '''
        This function populates the filmback text field
        '''
        info = self.data[self.camName][0]
        index = self.resField.currentIndex()
        fb = info[index][1]
        if self.checkBoxField.isChecked() is True:
            filmback = "{} x {} (in)".format(
                    str(float(fb[0])*2),
                    str(float(fb[1])*2))
            self.fbField.setText(filmback)
        else:
            filmback = "{} x {} (in)".format(fb[0], fb[1])
            self.fbField.setText(filmback)


def showUI():
    ui = CameraLibraryUI()
    ui.show()
    return ui


ui = showUI()
