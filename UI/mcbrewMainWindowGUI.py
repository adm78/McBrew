# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mcbrewMainWindowGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mcbrewMainWindow(object):
    def setupUi(self, mcbrewMainWindow):
        mcbrewMainWindow.setObjectName(_fromUtf8("mcbrewMainWindow"))
        mcbrewMainWindow.resize(1096, 753)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mcbrewMainWindow.sizePolicy().hasHeightForWidth())
        mcbrewMainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ferm_square.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mcbrewMainWindow.setWindowIcon(icon)
        self.mcbrewcentralwidget = QtGui.QWidget(mcbrewMainWindow)
        self.mcbrewcentralwidget.setObjectName(_fromUtf8("mcbrewcentralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mcbrewcentralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mcbrewhorizontalLayout = QtGui.QHBoxLayout()
        self.mcbrewhorizontalLayout.setObjectName(_fromUtf8("mcbrewhorizontalLayout"))
        self.verticalLayout.addLayout(self.mcbrewhorizontalLayout)
        self.vceplotArea = vcePlotWidget(self.mcbrewcentralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vceplotArea.sizePolicy().hasHeightForWidth())
        self.vceplotArea.setSizePolicy(sizePolicy)
        self.vceplotArea.setMouseTracking(False)
        self.vceplotArea.setObjectName(_fromUtf8("vceplotArea"))
        self.verticalLayout.addWidget(self.vceplotArea)
        mcbrewMainWindow.setCentralWidget(self.mcbrewcentralwidget)
        self.mcbrewmenubar = QtGui.QMenuBar(mcbrewMainWindow)
        self.mcbrewmenubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.mcbrewmenubar.setObjectName(_fromUtf8("mcbrewmenubar"))
        self.mcbrewmenuFile = QtGui.QMenu(self.mcbrewmenubar)
        self.mcbrewmenuFile.setObjectName(_fromUtf8("mcbrewmenuFile"))
        self.menuEdit = QtGui.QMenu(self.mcbrewmenubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.mcbrewmenubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        mcbrewMainWindow.setMenuBar(self.mcbrewmenubar)
        self.mcbrewtoolBar = QtGui.QToolBar(mcbrewMainWindow)
        self.mcbrewtoolBar.setIconSize(QtCore.QSize(50, 50))
        self.mcbrewtoolBar.setObjectName(_fromUtf8("mcbrewtoolBar"))
        mcbrewMainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.mcbrewtoolBar)
        self.mcbrewactionOpen = QtGui.QAction(mcbrewMainWindow)
        self.mcbrewactionOpen.setObjectName(_fromUtf8("mcbrewactionOpen"))
        self.actionSettings = QtGui.QAction(mcbrewMainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionFlash_tank = QtGui.QAction(mcbrewMainWindow)
        self.actionFlash_tank.setObjectName(_fromUtf8("actionFlash_tank"))
        self.mcbrewActionViewTherm = QtGui.QAction(mcbrewMainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/ferm_plus_therm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mcbrewActionViewTherm.setIcon(icon2)
        self.mcbrewActionViewTherm.setObjectName(_fromUtf8("mcbrewActionViewTherm"))
        self.mcbrewactionQuit = QtGui.QAction(mcbrewMainWindow)
        self.mcbrewactionQuit.setObjectName(_fromUtf8("mcbrewactionQuit"))
        self.vceactionSineWave = QtGui.QAction(mcbrewMainWindow)
        self.vceactionSineWave.setObjectName(_fromUtf8("vceactionSineWave"))
        self.vceactionCosineWave = QtGui.QAction(mcbrewMainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sine_wave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vceactionCosineWave.setIcon(icon3)
        self.vceactionCosineWave.setObjectName(_fromUtf8("vceactionCosineWave"))
        self.actionCosine_Wave = QtGui.QAction(mcbrewMainWindow)
        self.actionCosine_Wave.setObjectName(_fromUtf8("actionCosine_Wave"))
        self.mcbrewmenuFile.addAction(self.mcbrewactionOpen)
        self.mcbrewmenuFile.addSeparator()
        self.mcbrewmenuFile.addAction(self.mcbrewactionQuit)
        self.menuEdit.addAction(self.actionSettings)
        self.mcbrewmenubar.addAction(self.mcbrewmenuFile.menuAction())
        self.mcbrewmenubar.addAction(self.menuEdit.menuAction())
        self.mcbrewmenubar.addAction(self.menuView.menuAction())
        self.mcbrewtoolBar.addAction(self.mcbrewActionViewTherm)

        self.retranslateUi(mcbrewMainWindow)
        QtCore.QMetaObject.connectSlotsByName(mcbrewMainWindow)

    def retranslateUi(self, mcbrewMainWindow):
        mcbrewMainWindow.setWindowTitle(_translate("mcbrewMainWindow", "mcbrew", None))
        self.mcbrewmenuFile.setTitle(_translate("mcbrewMainWindow", "File", None))
        self.menuEdit.setTitle(_translate("mcbrewMainWindow", "Edit", None))
        self.menuView.setTitle(_translate("mcbrewMainWindow", "View", None))
        self.mcbrewtoolBar.setWindowTitle(_translate("mcbrewMainWindow", "toolBar", None))
        self.mcbrewactionOpen.setText(_translate("mcbrewMainWindow", "Open", None))
        self.actionSettings.setText(_translate("mcbrewMainWindow", "Settings", None))
        self.actionFlash_tank.setText(_translate("mcbrewMainWindow", "Flash tank", None))
        self.mcbrewActionViewTherm.setText(_translate("mcbrewMainWindow", "Flash Tank", None))
        self.mcbrewactionQuit.setText(_translate("mcbrewMainWindow", "Exit", None))
        self.vceactionSineWave.setText(_translate("mcbrewMainWindow", "Sine Wave", None))
        self.vceactionCosineWave.setText(_translate("mcbrewMainWindow", "Cosine Wave", None))
        self.actionCosine_Wave.setText(_translate("mcbrewMainWindow", "Cosine Wave", None))

from vceplotwidget import vcePlotWidget
import mcbrewGUIresources_rc
