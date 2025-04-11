# Form implementation generated from reading ui file 'mp3.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        MainWindow.setMaximumSize(QtCore.QSize(400, 450))
        MainWindow.setStyleSheet("* {\n"
"background:rgb(20, 22, 27);\n"
"color:#fff;\n"
"font-size:15px;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"border:1px solid #363947;\n"
"}\n"
"\n"
"QToolButton {\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #fff;\n"
"border: none;\n"
"}\n"
"QToolButton::hover {\n"
"background: rgba(255, 255, 255, 18);\n"
"color: #fff;\n"
"}\n"
"QToolButton::selected {\n"
"background: rgba(255, 255, 255, 40);\n"
"color: #fff;\n"
"}\n"
"QToolButton::pressed {\n"
"background: rgba(255, 255, 255, 40);\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton {\n"
"background: rgba(255, 255, 255, 0);\n"
"color: #fff;\n"
"border: none;\n"
"}\n"
"QPushButton::hover {\n"
"background: rgba(255, 255, 255, 18);\n"
"color: #fff;\n"
"}\n"
"QPushButton::pressed {\n"
"background: rgba(255, 255, 255, 40);\n"
"color: #fff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background: #202020;\n"
"color: #415f91;\n"
"border-radius: 12px;\n"
"border: 2px solid #d6e3ff;\n"
"padding: 10px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"background: rgba(255, 255, 255, 0);\n"
"height: 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background:rgba(255, 255, 255, 0);\n"
"width: 20px;\n"
"margin:0px -10px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background:#5da7ff;\n"
"height: 10px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background:#22252c;\n"
"height: 10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"border:none;\n"
"background: #14161b;\n"
"height: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"background:#363947;\n"
"min-width: 20px;\n"
"margin:2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"border:none;\n"
"background: #14161b;\n"
"width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:#363947;\n"
"min-height: 20px;\n"
"margin-top:10px;\n"
"margin-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"background:none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.list = QtWidgets.QWidget()
        self.list.setObjectName("list")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.list)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 465, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.list)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_6 = QtWidgets.QToolButton(parent=self.list)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_4.addWidget(self.toolButton_6)
        self.toolButton_4 = QtWidgets.QToolButton(parent=self.list)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_4.addWidget(self.toolButton_4)
        self.toolButton_5 = QtWidgets.QToolButton(parent=self.list)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_4.addWidget(self.toolButton_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.list)
        self.compact = QtWidgets.QWidget()
        self.compact.setObjectName("compact")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.compact)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.compact_preivew_img = QtWidgets.QWidget(parent=self.compact)
        self.compact_preivew_img.setMinimumSize(QtCore.QSize(100, 56))
        self.compact_preivew_img.setMaximumSize(QtCore.QSize(100, 56))
        self.compact_preivew_img.setObjectName("compact_preivew_img")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.compact_preivew_img)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.compact_layout_volume = QtWidgets.QHBoxLayout()
        self.compact_layout_volume.setSpacing(0)
        self.compact_layout_volume.setObjectName("compact_layout_volume")
        self.horizontalLayout_8.addLayout(self.compact_layout_volume)
        self.horizontalLayout_7.addWidget(self.compact_preivew_img)
        self.compact_layout_name = QtWidgets.QVBoxLayout()
        self.compact_layout_name.setObjectName("compact_layout_name")
        self.horizontalLayout_7.addLayout(self.compact_layout_name)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.compact_btn_repeat = QtWidgets.QToolButton(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compact_btn_repeat.sizePolicy().hasHeightForWidth())
        self.compact_btn_repeat.setSizePolicy(sizePolicy)
        self.compact_btn_repeat.setMinimumSize(QtCore.QSize(30, 30))
        self.compact_btn_repeat.setMaximumSize(QtCore.QSize(50, 16777215))
        self.compact_btn_repeat.setStyleSheet("* {\n"
"font-size:16px;\n"
"font:bold;\n"
"}\n"
"QToolButton::checked{\n"
"background:rgba(255, 255, 255, 30);\n"
"}")
        self.compact_btn_repeat.setCheckable(True)
        self.compact_btn_repeat.setChecked(False)
        self.compact_btn_repeat.setObjectName("compact_btn_repeat")
        self.horizontalLayout_5.addWidget(self.compact_btn_repeat)
        self.compact_btn_back = QtWidgets.QToolButton(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compact_btn_back.sizePolicy().hasHeightForWidth())
        self.compact_btn_back.setSizePolicy(sizePolicy)
        self.compact_btn_back.setMinimumSize(QtCore.QSize(30, 30))
        self.compact_btn_back.setMaximumSize(QtCore.QSize(50, 16777215))
        self.compact_btn_back.setStyleSheet("font-size:16px;\n"
"font:bold;")
        self.compact_btn_back.setObjectName("compact_btn_back")
        self.horizontalLayout_5.addWidget(self.compact_btn_back)
        self.compact_btn_play = QtWidgets.QToolButton(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compact_btn_play.sizePolicy().hasHeightForWidth())
        self.compact_btn_play.setSizePolicy(sizePolicy)
        self.compact_btn_play.setMinimumSize(QtCore.QSize(30, 30))
        self.compact_btn_play.setMaximumSize(QtCore.QSize(50, 16777215))
        self.compact_btn_play.setStyleSheet("font-size:16px;\n"
"font:bold;")
        self.compact_btn_play.setObjectName("compact_btn_play")
        self.horizontalLayout_5.addWidget(self.compact_btn_play)
        self.compact_btn_next = QtWidgets.QToolButton(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compact_btn_next.sizePolicy().hasHeightForWidth())
        self.compact_btn_next.setSizePolicy(sizePolicy)
        self.compact_btn_next.setMinimumSize(QtCore.QSize(30, 30))
        self.compact_btn_next.setMaximumSize(QtCore.QSize(50, 16777215))
        self.compact_btn_next.setStyleSheet("font-size:16px;\n"
"font:bold;")
        self.compact_btn_next.setObjectName("compact_btn_next")
        self.horizontalLayout_5.addWidget(self.compact_btn_next)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.compact_btn_exit = QtWidgets.QToolButton(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compact_btn_exit.sizePolicy().hasHeightForWidth())
        self.compact_btn_exit.setSizePolicy(sizePolicy)
        self.compact_btn_exit.setStyleSheet("* {\n"
"font:bold;\n"
"}\n"
"QToolButton::hover {\n"
"background: rgba(255, 0, 0, 150);\n"
"}\n"
"QToolButton::pressed {\n"
"background: rgba(255, 0, 0, 255);\n"
"}")
        self.compact_btn_exit.setObjectName("compact_btn_exit")
        self.verticalLayout_4.addWidget(self.compact_btn_exit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.compact_btn_list = QtWidgets.QToolButton(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compact_btn_list.sizePolicy().hasHeightForWidth())
        self.compact_btn_list.setSizePolicy(sizePolicy)
        self.compact_btn_list.setStyleSheet("font:bold;")
        self.compact_btn_list.setObjectName("compact_btn_list")
        self.verticalLayout_4.addWidget(self.compact_btn_list)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.compact_slider_time = QtWidgets.QSlider(parent=self.compact)
        self.compact_slider_time.setMinimum(0)
        self.compact_slider_time.setMaximum(100)
        self.compact_slider_time.setSingleStep(1)
        self.compact_slider_time.setPageStep(0)
        self.compact_slider_time.setProperty("value", 0)
        self.compact_slider_time.setSliderPosition(0)
        self.compact_slider_time.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.compact_slider_time.setObjectName("compact_slider_time")
        self.horizontalLayout_9.addWidget(self.compact_slider_time)
        self.compact_label_time = QtWidgets.QLabel(parent=self.compact)
        self.compact_label_time.setStyleSheet("font-size:12px;\n"
"color: #bdcfff;")
        self.compact_label_time.setObjectName("compact_label_time")
        self.horizontalLayout_9.addWidget(self.compact_label_time)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.compact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 388, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.compact_layout_list = QtWidgets.QVBoxLayout()
        self.compact_layout_list.setSpacing(5)
        self.compact_layout_list.setObjectName("compact_layout_list")
        self.verticalLayout_5.addLayout(self.compact_layout_list)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.compact)
        self.player = QtWidgets.QWidget()
        self.player.setObjectName("player")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.player)
        self.layoutWidget_2.setGeometry(QtCore.QRect(100, 390, 151, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolButton_10 = QtWidgets.QToolButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_10.sizePolicy().hasHeightForWidth())
        self.toolButton_10.setSizePolicy(sizePolicy)
        self.toolButton_10.setObjectName("toolButton_10")
        self.horizontalLayout_6.addWidget(self.toolButton_10)
        self.toolButton_11 = QtWidgets.QToolButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_11.sizePolicy().hasHeightForWidth())
        self.toolButton_11.setSizePolicy(sizePolicy)
        self.toolButton_11.setObjectName("toolButton_11")
        self.horizontalLayout_6.addWidget(self.toolButton_11)
        self.toolButton_12 = QtWidgets.QToolButton(parent=self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_12.sizePolicy().hasHeightForWidth())
        self.toolButton_12.setSizePolicy(sizePolicy)
        self.toolButton_12.setObjectName("toolButton_12")
        self.horizontalLayout_6.addWidget(self.toolButton_12)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.player)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 50, 311, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(parent=self.player)
        self.frame_2.setGeometry(QtCore.QRect(80, 450, 221, 16))
        self.frame_2.setStyleSheet("background:rgba(255, 255, 255, 30);\n"
"border-radius: 7px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalSlider_2 = QtWidgets.QSlider(parent=self.frame_2)
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal {\n"
"background: rgba(255, 255, 255, 0);\n"
"height: 15px;\n"
"margin: 2px 0;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background:rgba(255, 255, 255, 255);\n"
"width: 15px;\n"
"border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background:rgba(255, 255, 255, 100);\n"
"height: 25px;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background:rgba(255, 255, 255, 0);\n"
"height: 15px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}")
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_7.addWidget(self.horizontalSlider_2)
        self.stackedWidget.addWidget(self.player)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.toolButton_6.setText(_translate("MainWindow", "⏪︎"))
        self.toolButton_4.setText(_translate("MainWindow", "⏸︎"))
        self.toolButton_5.setText(_translate("MainWindow", "⏩︎"))
        self.compact_btn_repeat.setText(_translate("MainWindow", "O"))
        self.compact_btn_back.setText(_translate("MainWindow", "<<"))
        self.compact_btn_play.setText(_translate("MainWindow", "|>"))
        self.compact_btn_next.setText(_translate("MainWindow", ">>"))
        self.compact_btn_exit.setText(_translate("MainWindow", "X"))
        self.compact_btn_list.setText(_translate("MainWindow", "V"))
        self.compact_label_time.setText(_translate("MainWindow", "00:00/00:00"))
        self.toolButton_10.setText(_translate("MainWindow", "⏪︎"))
        self.toolButton_11.setText(_translate("MainWindow", "⏸︎"))
        self.toolButton_12.setText(_translate("MainWindow", "⏩︎"))
