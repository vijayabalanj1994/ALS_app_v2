# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTextEdit, QWidget)
import gui_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1209, 744)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/main/NeroBioMark_Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_status = QLabel(self.centralwidget)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(0, 30))
        self.lb_status.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lb_status.setFont(font1)
        self.lb_status.setStyleSheet(u"QLabel {\n"
"    background-color: #F44336;  /* Medium red (Material Design red 500) */\n"
"    color: white;               /* White text for contrast */\n"
"    padding: 4px;\n"
"    border-radius: 3px;\n"
"}")

        self.gridLayout.addWidget(self.lb_status, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(425, 250))

        self.gridLayout_5.addWidget(self.textEdit, 2, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setMaximumSize(QSize(225, 16777215))
        self.groupBox_5.setSizeIncrement(QSize(0, 0))
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_region = QLineEdit(self.groupBox_5)
        self.lb_region.setObjectName(u"lb_region")
        self.lb_region.setMinimumSize(QSize(200, 30))
        self.lb_region.setMaximumSize(QSize(16777215, 30))
        self.lb_region.setFont(font1)
        self.lb_region.setStyleSheet(u"color: #FFC107;\n"
"")

        self.gridLayout_2.addWidget(self.lb_region, 12, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 30))
        self.label_18.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    background-color: #FFC107;  /* Amber (Material Design amber 500) */\n"
"    color: white;               /* White text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 25))
        self.label_5.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.label_5, 9, 0, 1, 1)

        self.lb_image_no = QLineEdit(self.groupBox_5)
        self.lb_image_no.setObjectName(u"lb_image_no")
        self.lb_image_no.setMinimumSize(QSize(200, 30))
        self.lb_image_no.setMaximumSize(QSize(16777215, 30))
        self.lb_image_no.setFont(font1)
        self.lb_image_no.setStyleSheet(u"color: #FFC107;\n"
"")

        self.gridLayout_2.addWidget(self.lb_image_no, 8, 0, 1, 1)

        self.pb_browse_image = QPushButton(self.groupBox_5)
        self.pb_browse_image.setObjectName(u"pb_browse_image")
        self.pb_browse_image.setFont(font1)
        self.pb_browse_image.setStyleSheet(u"color:#2196F3;")

        self.gridLayout_2.addWidget(self.pb_browse_image, 4, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"QLabel {\n"
"    background-color: #FFC107;  /* Amber (Material Design amber 500) */\n"
"    color: white;               /* White text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_19, 6, 0, 1, 1)

        self.lb_case_id = QLineEdit(self.groupBox_5)
        self.lb_case_id.setObjectName(u"lb_case_id")
        self.lb_case_id.setMinimumSize(QSize(200, 30))
        self.lb_case_id.setMaximumSize(QSize(16777215, 30))
        self.lb_case_id.setFont(font1)
        self.lb_case_id.setStyleSheet(u"color: #FFC107;\n"
"")

        self.gridLayout_2.addWidget(self.lb_case_id, 10, 0, 1, 1)

        self.lb_input_image = QLabel(self.groupBox_5)
        self.lb_input_image.setObjectName(u"lb_input_image")
        self.lb_input_image.setMinimumSize(QSize(200, 200))
        self.lb_input_image.setMaximumSize(QSize(200, 200))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.lb_input_image.setFont(font3)
        self.lb_input_image.setFrameShape(QFrame.WinPanel)
        self.lb_input_image.setScaledContents(True)
        self.lb_input_image.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_input_image, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 25))
        self.label_4.setMaximumSize(QSize(16777215, 25))
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 25))
        self.label_6.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.label_6, 11, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 3, 1)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(500, 280))
        self.groupBox_7.setMaximumSize(QSize(16777215, 300))
        self.groupBox_7.setFont(font1)
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_prediction = QLabel(self.groupBox_7)
        self.lb_prediction.setObjectName(u"lb_prediction")
        self.lb_prediction.setMinimumSize(QSize(0, 50))
        self.lb_prediction.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.lb_prediction.setFont(font4)
        self.lb_prediction.setStyleSheet(u"QLabel {\n"
"    background-color: #B71C1C;  /* Dark red */\n"
"    color: black;               /* Black text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.lb_prediction.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_prediction, 6, 2, 1, 2)

        self.p_bar_discordant = QProgressBar(self.groupBox_7)
        self.p_bar_discordant.setObjectName(u"p_bar_discordant")
        self.p_bar_discordant.setMinimumSize(QSize(0, 25))
        self.p_bar_discordant.setValue(0)

        self.gridLayout_3.addWidget(self.p_bar_discordant, 3, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"QLabel {\n"
"    background-color: #4CAF50;  /* Medium green */\n"
"    color: white;               /* White text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_20, 5, 2, 1, 2)

        self.lb_cam_image = QLabel(self.groupBox_7)
        self.lb_cam_image.setObjectName(u"lb_cam_image")
        self.lb_cam_image.setMinimumSize(QSize(200, 200))
        self.lb_cam_image.setMaximumSize(QSize(200, 200))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        self.lb_cam_image.setFont(font5)
        self.lb_cam_image.setFrameShape(QFrame.WinPanel)
        self.lb_cam_image.setScaledContents(True)
        self.lb_cam_image.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_cam_image, 1, 0, 7, 2)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 25))
        self.label_15.setFont(font1)

        self.gridLayout_3.addWidget(self.label_15, 1, 2, 1, 1)

        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 5))

        self.gridLayout_3.addWidget(self.label_21, 4, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"QLabel {\n"
"    background-color: #4CAF50;  /* Medium green */\n"
"    color: white;               /* White text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 2)

        self.p_bar_control = QProgressBar(self.groupBox_7)
        self.p_bar_control.setObjectName(u"p_bar_control")
        self.p_bar_control.setMinimumSize(QSize(0, 25))
        self.p_bar_control.setValue(0)

        self.gridLayout_3.addWidget(self.p_bar_control, 1, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(100, 25))
        self.label_17.setFont(font1)

        self.gridLayout_3.addWidget(self.label_17, 3, 2, 1, 1)

        self.p_bar_concordant = QProgressBar(self.groupBox_7)
        self.p_bar_concordant.setObjectName(u"p_bar_concordant")
        self.p_bar_concordant.setMinimumSize(QSize(0, 25))
        self.p_bar_concordant.setValue(0)

        self.gridLayout_3.addWidget(self.p_bar_concordant, 2, 3, 1, 1)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(100, 25))
        self.label_16.setFont(font1)

        self.gridLayout_3.addWidget(self.label_16, 2, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"QLabel {\n"
"    background-color: #4CAF50;  /* Medium green */\n"
"    color: white;               /* White text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")

        self.gridLayout_3.addWidget(self.label_13, 0, 2, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 8, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 3)

        self.lb_filtered_image = QLabel(self.groupBox_2)
        self.lb_filtered_image.setObjectName(u"lb_filtered_image")
        self.lb_filtered_image.setMinimumSize(QSize(400, 400))
        self.lb_filtered_image.setMaximumSize(QSize(400, 400))
        self.lb_filtered_image.setFont(font3)
        self.lb_filtered_image.setFrameShape(QFrame.WinPanel)
        self.lb_filtered_image.setScaledContents(True)
        self.lb_filtered_image.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_filtered_image, 0, 0, 1, 3)

        self.pb_run_analysis = QPushButton(self.groupBox_2)
        self.pb_run_analysis.setObjectName(u"pb_run_analysis")
        self.pb_run_analysis.setFont(font1)
        self.pb_run_analysis.setStyleSheet(u"color:#2196F3;")

        self.gridLayout_4.addWidget(self.pb_run_analysis, 6, 0, 1, 1)

        self.pb_clear = QPushButton(self.groupBox_2)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setFont(font1)
        self.pb_clear.setStyleSheet(u"color:#2196F3;")

        self.gridLayout_4.addWidget(self.pb_clear, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.s_filter_slider = QSlider(self.groupBox_2)
        self.s_filter_slider.setObjectName(u"s_filter_slider")
        self.s_filter_slider.setMaximumSize(QSize(16777215, 25))
        self.s_filter_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.s_filter_slider, 2, 0, 1, 3)

        self.pb_export_results = QPushButton(self.groupBox_2)
        self.pb_export_results.setObjectName(u"pb_export_results")
        self.pb_export_results.setFont(font1)
        self.pb_export_results.setStyleSheet(u"color:#2196F3;\n"
"")

        self.gridLayout_4.addWidget(self.pb_export_results, 6, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"QLabel {\n"
"	background-color:#2196F3 ;\n"
"    color: black;               /* Black text */\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 5, 0, 1, 3)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 2, 3, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1209, 34))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ALS Diagnostic Assistant", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"Status: Waiting for Image", None))
        self.groupBox.setTitle("")
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your notes or observations here...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Case ID:", None))
        self.pb_browse_image.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Meta Data", None))
        self.lb_input_image.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Image No:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.lb_prediction.setText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Model Prediction:", None))
        self.lb_cam_image.setText(QCoreApplication.translate("MainWindow", u"Waiting for modal to run...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Control:", None))
        self.label_21.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CAM Overlay Image", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Discordant:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Concordant:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Model Analytics:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"CAM Overlay Image Viewer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Adjust Heatmap Overlay Focus ", None))
        self.lb_filtered_image.setText(QCoreApplication.translate("MainWindow", u"Waiting for model to run...", None))
        self.pb_run_analysis.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pb_export_results.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
    # retranslateUi

