
from PyQt5 import QtCore, QtGui, QtWidgets
from ASCII import *
from time import time
import datetime
import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog
from PyQt5.uic import loadUi
from os import walk

class Ui_alphy_pix2symb_converter(object):
    def setupUi(self, alphy_pix2symb_converter):
        alphy_pix2symb_converter.setObjectName("alphy_pix2symb_converter")
        alphy_pix2symb_converter.resize(520, 233)
        alphy_pix2symb_converter.setMinimumSize(QtCore.QSize(520, 233))
        alphy_pix2symb_converter.setMaximumSize(QtCore.QSize(520, 233))

        # DIMENSION BOX FRAME
        #=====================
        self.frame_dimension = QtWidgets.QFrame(alphy_pix2symb_converter)
        self.frame_dimension.setGeometry(QtCore.QRect(10, 50, 91, 171))
        self.frame_dimension.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_dimension.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dimension.setLineWidth(3)
        self.frame_dimension.setObjectName("frame_dimension")

        # LABEL WIDTH
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.frame_dimension)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 73, 51))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")

        self.gridLayout_width = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_width.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_width.setObjectName("gridLayout_width")

        self.label_width = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_width.setMinimumSize(QtCore.QSize(0, 20))
        self.label_width.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_width.setFont(font)
        self.label_width.setObjectName("label_width")
        self.gridLayout_width.addWidget(self.label_width, 0, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.lineEdit_width = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.gridLayout_width.addWidget(self.lineEdit_width, 1, 0, 1, 1)

        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_dimension)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 73, 51))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")

        self.gridLayout_hight = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_hight.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_hight.setObjectName("gridLayout_hight")

        self.label_hight = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_hight.setMinimumSize(QtCore.QSize(0, 20))
        self.label_hight.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_hight.setFont(font)
        self.label_hight.setObjectName("label_hight")
        self.gridLayout_hight.addWidget(self.label_hight, 0, 0, 1, 1, QtCore.Qt.AlignLeft)

        # LABEL SCALE
        self.lineEdit_hight = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_hight.setObjectName("lineEdit_hight")
        self.gridLayout_hight.addWidget(self.lineEdit_hight, 1, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame_dimension)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 110, 73, 51))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_scale = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_scale.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_scale.setObjectName("gridLayout_scale")
        self.label_scale = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_scale.setMinimumSize(QtCore.QSize(0, 20))
        self.label_scale.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_scale.setFont(font)
        self.label_scale.setObjectName("label_scale")
        self.gridLayout_scale.addWidget(self.label_scale, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lineEdit_scale = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_scale.setObjectName("lineEdit_scale")
        self.gridLayout_scale.addWidget(self.lineEdit_scale, 1, 0, 1, 1)

        # ADDRESS BOX FRAME
        #===================
        self.frame_address_box = QtWidgets.QFrame(alphy_pix2symb_converter)
        self.frame_address_box.setGeometry(QtCore.QRect(110, 50, 301, 171))
        self.frame_address_box.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_address_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_address_box.setLineWidth(3)
        self.frame_address_box.setObjectName("frame_address_box")

        # SOURCE ADDRESS
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_address_box)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 281, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

        self.gridLayout_usesymb = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_usesymb.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_usesymb.setObjectName("gridLayout_usesymb")

        self.label_usesymb = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_usesymb.setMinimumSize(QtCore.QSize(0, 20))
        self.label_usesymb.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_usesymb.setFont(font)
        self.label_usesymb.setObjectName("label_usesymb")
        self.gridLayout_usesymb.addWidget(self.label_usesymb, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lineEdit_symb_use = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_symb_use.setObjectName("lineEdit_symb_use")
        self.gridLayout_usesymb.addWidget(self.lineEdit_symb_use, 1, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame_address_box)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 110, 281, 51))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_saveadd = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_saveadd.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_saveadd.setObjectName("gridLayout_saveadd")
        self.label_saveadd = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_saveadd.setMinimumSize(QtCore.QSize(0, 20))
        self.label_saveadd.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_saveadd.setFont(font)
        self.label_saveadd.setObjectName("label_saveadd")
        self.gridLayout_saveadd.addWidget(self.label_saveadd, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lineEdit_save_address = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_save_address.setObjectName("lineEdit_save_address")
        self.gridLayout_saveadd.addWidget(self.lineEdit_save_address, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_address_box)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_sourceadd = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_sourceadd.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_sourceadd.setObjectName("gridLayout_sourceadd")
        self.lineEdit_source_add = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_source_add.setObjectName("lineEdit_source_add")
        self.gridLayout_sourceadd.addWidget(self.lineEdit_source_add, 1, 0, 1, 1)

        self.label_sourceadd = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_sourceadd.setMinimumSize(QtCore.QSize(0, 20))
        self.label_sourceadd.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_sourceadd.setFont(font)
        self.label_sourceadd.setObjectName("label_sourceadd")
        self.gridLayout_sourceadd.addWidget(self.label_sourceadd, 0, 0, 1, 1, QtCore.Qt.AlignLeft)

        # OPEN BUTTON
        self.pushButton_open = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_open.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_open.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout_sourceadd.addWidget(self.pushButton_open, 1, 1, 1, 1)

        # GENERATE BUTTON FRAME
        #=======================
        self.frame_generate_button = QtWidgets.QFrame(alphy_pix2symb_converter)
        self.frame_generate_button.setGeometry(QtCore.QRect(420, 50, 91, 171))
        self.frame_generate_button.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_generate_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_generate_button.setLineWidth(3)
        self.frame_generate_button.setObjectName("frame_generate_button")

        # GENERATE BUTTON
        self.pushButton_generate = QtWidgets.QPushButton(self.frame_generate_button)
        self.pushButton_generate.setGeometry(QtCore.QRect(10, 10, 75, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        self.pushButton_generate.setPalette(palette)
        self.pushButton_generate.setAutoFillBackground(True)
        self.pushButton_generate.setObjectName("pushButton_generate")


        self.frame_4 = QtWidgets.QFrame(alphy_pix2symb_converter)
        self.frame_4.setGeometry(QtCore.QRect(10, 0, 501, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(3)
        self.frame_4.setObjectName("frame_4")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, -1, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.Layout_header_text = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Layout_header_text.setContentsMargins(0, 0, 0, 0)
        self.Layout_header_text.setObjectName("Layout_header_text")

        self.label_header_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_header_text.setMinimumSize(QtCore.QSize(0, 20))
        self.label_header_text.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_header_text.setFont(font)
        self.label_header_text.setObjectName("label_header_text")
        self.Layout_header_text.addWidget(self.label_header_text, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(alphy_pix2symb_converter)
        self.label.setGeometry(QtCore.QRect(-20, -18, 581, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("BGW.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.frame_dimension.raise_()
        self.frame_address_box.raise_()
        self.frame_generate_button.raise_()
        self.frame_4.raise_()

        self.retranslateUi(alphy_pix2symb_converter)
        QtCore.QMetaObject.connectSlotsByName(alphy_pix2symb_converter)

    def retranslateUi(self, alphy_pix2symb_converter):
        _translate = QtCore.QCoreApplication.translate
        alphy_pix2symb_converter.setWindowTitle(_translate("alphy_pix2symb_converter",
                                                           "ALPHY PICTURE TO SYMBOLS CONVERTER"))
        self.label_width.setText(_translate("alphy_pix2symb_converter", "Width"))
        self.lineEdit_width.setText(_translate("alphy_pix2symb_converter", "350"))
        self.label_hight.setText(_translate("alphy_pix2symb_converter", "Hight"))
        self.lineEdit_hight.setText(_translate("alphy_pix2symb_converter", "350"))
        self.label_scale.setText(_translate("alphy_pix2symb_converter", "Scale"))
        self.lineEdit_scale.setText(_translate("alphy_pix2symb_converter", "60"))
        self.label_usesymb.setText(_translate("alphy_pix2symb_converter", "Use Symbols"))
        self.lineEdit_symb_use.setText(_translate("alphy_pix2symb_converter","Ñ%&=HAIM3Y"))
        self.label_saveadd.setText(_translate("alphy_pix2symb_converter", "Save Address"))
        self.lineEdit_save_address.setText(_translate("alphy_pix2symb_converter",
                                                      "It is Automatic & it Will save in the source folder"))
        self.lineEdit_source_add.setText(_translate("alphy_pix2symb_converter", " "))
        self.label_sourceadd.setText(_translate("alphy_pix2symb_converter", "Source Address"))
        self.pushButton_open.setText(_translate("alphy_pix2symb_converter", "Open"))
        self.pushButton_generate.setText(_translate("alphy_pix2symb_converter", "GENERATE"))
        self.label_header_text.setText(_translate("alphy_pix2symb_converter", "ALPHY PICTURE TO SYMBOLS CONVERTER"))
        self.pushButton_generate.clicked.connect( lambda : self.myconvert())
        self.pushButton_open.clicked.connect( lambda : self.Browse_files())

    def myconvert(self):
        self.lineEdit_save_address.setText("It is Automatic & it Will save in the source folder")

        width = int(self.lineEdit_width.text())
        hight = int(self.lineEdit_hight.text())
        scale = int(self.lineEdit_scale.text())
        address = self.lineEdit_source_add.text()

        folder_add_split = address.split("\\")
        add_len = len(folder_add_split)
        new_add =  "\\".join(folder_add_split [:-1])
        new_file_name = folder_add_split[-1]
        new_name_split = new_file_name.split(".")


        n = 1
        new_correct_name = new_name_split[0] + "_New_Version_" + str(n) + " [" + str(width) + "X" + str(hight) +\
                           "-" + str(scale) + "X]" + "." + new_name_split[1]
        dir_path = new_add
        res = []
        for (dir_path, dir_names, file_names) in walk(dir_path):
            res.extend(file_names)
        while new_correct_name in res[:]:
            n += 1
            new_correct_name = new_name_split[0]+ "_New_Version_" + str(n) + " [" + str(width) + "X" + str(hight) +\
                               "-" + str(scale) + "X]" + "." + new_name_split[1]
        else:
            new_correct_name = new_name_split[0]+ "_New_Version_" + str(n) + " [" + str(width) + "X" + str(hight) +\
                               "-" + str(scale) + "X]" + "." + new_name_split[1]

        final_add = [new_add, new_correct_name]
        final_new_add = "\\".join(final_add)
        self.lineEdit_save_address.setText(final_new_add)

        save_to = final_new_add
        Symbols = self.lineEdit_symb_use.text()

        print("--------------------------------")
        print("ALPHY PICTURE TO SYMBOLS CONVERTER")
        print("--------------------------------")
        print('The Resolution is:', width, " X ", hight)
        print('The Scale is:', scale , "X")
        print("--------------------------------")
        start_time = datetime.datetime.now().strftime
        print('The start time is:', start_time ("%H:%M:%S"))
        print("Please Wait ... ")
        nows = time()
        print("--------------------------------")
        width2 = width
        hight2 = hight
        characters = density_sorter(Symbols, 'arial', (width, hight))
        picture_to_ascii_rgb(address, final_new_add, characters, (width2, hight2), scale=scale,
                                                                font='C:\\Windows\\Fonts\\BRLNSB.TTF')
        end_time = datetime.datetime.now().strftime
        nowe = time()
        difference = nowe - nows
        minutes = difference / 60
        seconds = difference % 60
        print("* Done!, It takes " , int(minutes),":" ,int(seconds), " to generate your file")
        print("--------------------------------")
        print("Your file saved in : " + save_to)
        print("--------------------------------")
        os.startfile(new_add)
        os.startfile(final_new_add)

    def Browse_files(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        file_name = QFileDialog.getOpenFileName()
        path2 = file_name[0]
        path = path2.replace("/", "\\")
        address = path
        source_addresss = path
        self.lineEdit_source_add.setText(path)
        self.lineEdit_save_address.setText("It is Automatic & it Will save in the source folder")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    alphy_pix2symb_converter = QtWidgets.QWidget()
    ui = Ui_alphy_pix2symb_converter()
    ui.setupUi(alphy_pix2symb_converter)
    alphy_pix2symb_converter.show()
    sys.exit(app.exec_())

