import json
from qtpy import QtWidgets, QtGui, QtCore


class CameraLibraryUI(QtWidgets.QDialog):

    def __init__(self):
        super(CameraLibraryUI, self).__init__()
        self.data = self.loadData()
        self.setWindowTitle("Camera Libray UI")
        self.setFixedSize(500, 100)
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

        camLayout.addWidget(self.cameraField)
        camLayout.addWidget(self.resField)

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
        with open("data/data.json", "r") as f:
            data = json.load(f)
        return data

    def populateRes_Field(self):
        '''
        This fuction populates the resolution field
        '''
        self.resField.clear()
        self.camName = self.cameraField.currentText()
        for i, k in self.data[self.camName][0]:
            resolution = "{} x {}".format(i[0], i[1])
            self.resField.addItem(resolution)

    def populateTextField(self):
        '''
        This function populates the filmback text field
        '''
        info = self.data[self.camName][0]
        index = self.resField.currentIndex()
        fb = info[index][1]
        filmback = "{} x {} (in)".format(fb[0], fb[1])
        self.fbField.setText(filmback)


def showUI():
    ui = CameraLibraryUI()
    ui.show()
    return ui


ui = showUI()
