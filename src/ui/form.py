# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 485)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 485))
        MainWindow.setMaximumSize(QtCore.QSize(700, 485))
        MainWindow.setMouseTracking(False)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 681, 471))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.pushButtonStartScan = QtWidgets.QPushButton(parent=self.Home)
        self.pushButtonStartScan.setEnabled(False)
        self.pushButtonStartScan.setGeometry(QtCore.QRect(10, 390, 111, 41))
        self.pushButtonStartScan.setObjectName("pushButtonStartScan")
        self.groupBox = QtWidgets.QGroupBox(parent=self.Home)
        self.groupBox.setGeometry(QtCore.QRect(270, 100, 151, 251))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_23 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_23)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelAchievementCountProcessed = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelAchievementCountProcessed.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed.setObjectName("labelAchievementCountProcessed")
        self.horizontalLayout_2.addWidget(self.labelAchievementCountProcessed)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.labelAchievementCount = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount.setObjectName("labelAchievementCount")
        self.horizontalLayout_2.addWidget(self.labelAchievementCount)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)
        self.label_24 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_24)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelAchievementCountProcessed_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_2.setObjectName("labelAchievementCountProcessed_2")
        self.horizontalLayout_3.addWidget(self.labelAchievementCountProcessed_2)
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.labelAchievementCount_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_2.setObjectName("labelAchievementCount_2")
        self.horizontalLayout_3.addWidget(self.labelAchievementCount_2)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)
        self.label_25 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_25)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelAchievementCountProcessed_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_3.setObjectName("labelAchievementCountProcessed_3")
        self.horizontalLayout_4.addWidget(self.labelAchievementCountProcessed_3)
        self.label_14 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.labelAchievementCount_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_3.setObjectName("labelAchievementCount_3")
        self.horizontalLayout_4.addWidget(self.labelAchievementCount_3)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelAchievementCountProcessed_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_4.setObjectName("labelAchievementCountProcessed_4")
        self.horizontalLayout_7.addWidget(self.labelAchievementCountProcessed_4)
        self.label_17 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.labelAchievementCount_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_4.setObjectName("labelAchievementCount_4")
        self.horizontalLayout_7.addWidget(self.labelAchievementCount_4)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_7)
        self.label_26 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_26)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelAchievementCountProcessed_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_5.setObjectName("labelAchievementCountProcessed_5")
        self.horizontalLayout_8.addWidget(self.labelAchievementCountProcessed_5)
        self.label_18 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.labelAchievementCount_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_5.setObjectName("labelAchievementCount_5")
        self.horizontalLayout_8.addWidget(self.labelAchievementCount_5)
        self.formLayout_3.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelAchievementCountProcessed_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_6.setObjectName("labelAchievementCountProcessed_6")
        self.horizontalLayout_9.addWidget(self.labelAchievementCountProcessed_6)
        self.label_19 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_9.addWidget(self.label_19)
        self.labelAchievementCount_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_6.setObjectName("labelAchievementCount_6")
        self.horizontalLayout_9.addWidget(self.labelAchievementCount_6)
        self.formLayout_3.setLayout(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelAchievementCountProcessed_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_7.setObjectName("labelAchievementCountProcessed_7")
        self.horizontalLayout_10.addWidget(self.labelAchievementCountProcessed_7)
        self.label_20 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_10.addWidget(self.label_20)
        self.labelAchievementCount_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_7.setObjectName("labelAchievementCount_7")
        self.horizontalLayout_10.addWidget(self.labelAchievementCount_7)
        self.formLayout_3.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.labelAchievementCountProcessed_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_8.setObjectName("labelAchievementCountProcessed_8")
        self.horizontalLayout_11.addWidget(self.labelAchievementCountProcessed_8)
        self.label_21 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_11.addWidget(self.label_21)
        self.labelAchievementCount_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_8.setObjectName("labelAchievementCount_8")
        self.horizontalLayout_11.addWidget(self.labelAchievementCount_8)
        self.formLayout_3.setLayout(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelAchievementCountProcessed_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCountProcessed_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelAchievementCountProcessed_9.setObjectName("labelAchievementCountProcessed_9")
        self.horizontalLayout_12.addWidget(self.labelAchievementCountProcessed_9)
        self.label_22 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.labelAchievementCount_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.labelAchievementCount_9.setObjectName("labelAchievementCount_9")
        self.horizontalLayout_12.addWidget(self.labelAchievementCount_9)
        self.formLayout_3.setLayout(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_12)
        self.label_27 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_27)
        self.label_28 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_28)
        self.label_29 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_29)
        self.label_30 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_30)
        self.label_31 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_31)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.Home)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 411, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 391, 56))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonOpenLocation = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonOpenLocation.setObjectName("pushButtonOpenLocation")
        self.gridLayout.addWidget(self.pushButtonOpenLocation, 1, 1, 1, 1)
        self.pushButtonChangeLocation = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonChangeLocation.setObjectName("pushButtonChangeLocation")
        self.gridLayout.addWidget(self.pushButtonChangeLocation, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.lineEditOutputLocation = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.lineEditOutputLocation.setObjectName("lineEditOutputLocation")
        self.gridLayout.addWidget(self.lineEditOutputLocation, 0, 0, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.Home)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 10, 231, 421))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 211, 391))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.Home)
        self.label.setGeometry(QtCore.QRect(240, 390, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.Home)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 100, 251, 251))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEditLog = QtWidgets.QPlainTextEdit(parent=self.groupBox_5)
        self.textEditLog.setGeometry(QtCore.QRect(10, 20, 231, 221))
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        self.comboBoxMode = QtWidgets.QComboBox(parent=self.Home)
        self.comboBoxMode.setGeometry(QtCore.QRect(130, 400, 101, 24))
        self.comboBoxMode.setObjectName("comboBoxMode")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.comboBoxScanner = QtWidgets.QComboBox(parent=self.Home)
        self.comboBoxScanner.setGeometry(QtCore.QRect(130, 360, 101, 24))
        self.comboBoxScanner.setObjectName("comboBoxScanner")
        self.comboBoxScanner.addItem("")
        self.label_2 = QtWidgets.QLabel(parent=self.Home)
        self.label_2.setGeometry(QtCore.QRect(20, 350, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.Home)
        self.label_3.setGeometry(QtCore.QRect(240, 350, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBoxLanguage = QtWidgets.QComboBox(parent=self.Home)
        self.comboBoxLanguage.setGeometry(QtCore.QRect(320, 360, 101, 24))
        self.comboBoxLanguage.setObjectName("comboBoxLanguage")
        self.comboBoxLanguage.addItem("")
        self.tabWidget.addTab(self.Home, "")
        self.Configure = QtWidgets.QWidget()
        self.Configure.setObjectName("Configure")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 170, 131, 61))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButtonRestoreDefaults = QtWidgets.QPushButton(parent=self.groupBox_7)
        self.pushButtonRestoreDefaults.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.pushButtonRestoreDefaults.setObjectName("pushButtonRestoreDefaults")
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 110, 201, 51))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_8)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxDebugMode = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBoxDebugMode.setObjectName("checkBoxDebugMode")
        self.verticalLayout_2.addWidget(self.checkBoxDebugMode)
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.Configure)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 411, 91))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_9)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 391, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalScrollBarScanDelay = QtWidgets.QScrollBar(parent=self.gridLayoutWidget_2)
        self.horizontalScrollBarScanDelay.setMaximum(5000)
        self.horizontalScrollBarScanDelay.setSingleStep(100)
        self.horizontalScrollBarScanDelay.setPageStep(1000)
        self.horizontalScrollBarScanDelay.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBarScanDelay.setObjectName("horizontalScrollBarScanDelay")
        self.gridLayout_2.addWidget(self.horizontalScrollBarScanDelay, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.spinBoxNavDelay = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_2)
        self.spinBoxNavDelay.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spinBoxNavDelay.setWrapping(False)
        self.spinBoxNavDelay.setFrame(True)
        self.spinBoxNavDelay.setReadOnly(False)
        self.spinBoxNavDelay.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBoxNavDelay.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxNavDelay.setProperty("showGroupSeparator", False)
        self.spinBoxNavDelay.setSuffix("")
        self.spinBoxNavDelay.setMinimum(0)
        self.spinBoxNavDelay.setMaximum(100000)
        self.spinBoxNavDelay.setSingleStep(100)
        self.spinBoxNavDelay.setProperty("value", 0)
        self.spinBoxNavDelay.setObjectName("spinBoxNavDelay")
        self.gridLayout_2.addWidget(self.spinBoxNavDelay, 0, 2, 1, 1)
        self.spinBoxScanDelay = QtWidgets.QSpinBox(parent=self.gridLayoutWidget_2)
        self.spinBoxScanDelay.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.spinBoxScanDelay.setMaximum(100000)
        self.spinBoxScanDelay.setSingleStep(100)
        self.spinBoxScanDelay.setProperty("value", 0)
        self.spinBoxScanDelay.setObjectName("spinBoxScanDelay")
        self.gridLayout_2.addWidget(self.spinBoxScanDelay, 1, 2, 1, 1)
        self.horizontalScrollBarNavDelay = QtWidgets.QScrollBar(parent=self.gridLayoutWidget_2)
        self.horizontalScrollBarNavDelay.setSizeIncrement(QtCore.QSize(0, 0))
        self.horizontalScrollBarNavDelay.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.horizontalScrollBarNavDelay.setMaximum(5000)
        self.horizontalScrollBarNavDelay.setSingleStep(100)
        self.horizontalScrollBarNavDelay.setPageStep(1000)
        self.horizontalScrollBarNavDelay.setProperty("value", 0)
        self.horizontalScrollBarNavDelay.setSliderPosition(0)
        self.horizontalScrollBarNavDelay.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalScrollBarNavDelay.setInvertedAppearance(False)
        self.horizontalScrollBarNavDelay.setObjectName("horizontalScrollBarNavDelay")
        self.gridLayout_2.addWidget(self.horizontalScrollBarNavDelay, 0, 1, 1, 1)
        self.tabWidget.addTab(self.Configure, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalScrollBarScanDelay.valueChanged['int'].connect(self.spinBoxScanDelay.setValue) # type: ignore
        self.spinBoxNavDelay.valueChanged['int'].connect(self.horizontalScrollBarNavDelay.setValue) # type: ignore
        self.spinBoxScanDelay.valueChanged['int'].connect(self.horizontalScrollBarScanDelay.setValue) # type: ignore
        self.horizontalScrollBarNavDelay.valueChanged['int'].connect(self.spinBoxNavDelay.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HSR Achievement Scanner 1.0"))
        self.pushButtonStartScan.setText(_translate("MainWindow", "Start Scan"))
        self.groupBox.setTitle(_translate("MainWindow", "Item count"))
        self.label_23.setText(_translate("MainWindow", "Tab 1"))
        self.labelAchievementCountProcessed.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "Tab 2"))
        self.labelAchievementCountProcessed_2.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_2.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "Tab 3"))
        self.labelAchievementCountProcessed_3.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_3.setText(_translate("MainWindow", "0"))
        self.labelAchievementCountProcessed_4.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_4.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "Tab 4"))
        self.labelAchievementCountProcessed_5.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_5.setText(_translate("MainWindow", "0"))
        self.labelAchievementCountProcessed_6.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_6.setText(_translate("MainWindow", "0"))
        self.labelAchievementCountProcessed_7.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_7.setText(_translate("MainWindow", "0"))
        self.labelAchievementCountProcessed_8.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_8.setText(_translate("MainWindow", "0"))
        self.labelAchievementCountProcessed_9.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "/"))
        self.labelAchievementCount_9.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "Tab 5"))
        self.label_28.setText(_translate("MainWindow", "Tab 6"))
        self.label_29.setText(_translate("MainWindow", "Tab 7"))
        self.label_30.setText(_translate("MainWindow", "Tab 8"))
        self.label_31.setText(_translate("MainWindow", "Tab 9"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output location"))
        self.pushButtonOpenLocation.setText(_translate("MainWindow", "Open Folder"))
        self.pushButtonChangeLocation.setText(_translate("MainWindow", "Change"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Info"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; text-decoration: underline;\">HSR ACHIEVEMENT SCANNER</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; text-decoration: underline;\">HOW TO RUN</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">1. Set resolution with aspect ratio 16:9 (such as 1920x1080)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">2. Choose what to scan. Customize OCR Method and language if needed.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">3. If scanning achievements: Open cellphone menu (ESC) go to achievements, and go in the first tab (I, Trailblazer) (The achievements have to be visible, you have to be at the top.)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">3 bis. If scanning bookshelf: go to the first tab, be sure the first book is selected</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">4. Press the start scan button</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">5. Don\'t move mouse, click or press any key during the scan process.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; text-decoration: underline;\">NOTES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">- Database is updated separately from this app. If the database version doesn\'t match the latest game version, then the database hasn\'t been updated yet. You will need to check again later.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">HSRAchievementScanner is not affiliated with, endorsed, sponsored, or approved by HoYoverse.</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Press ALT + TAB to cancel"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Log"))
        self.comboBoxMode.setCurrentText(_translate("MainWindow", "Achievements"))
        self.comboBoxMode.setItemText(0, _translate("MainWindow", "Achievements"))
        self.comboBoxMode.setItemText(1, _translate("MainWindow", "Bookshelf"))
        self.comboBoxScanner.setToolTip(_translate("MainWindow", "<html><head/><body><p>Choose the method that yields the best results.</p></body></html>"))
        self.comboBoxScanner.setCurrentText(_translate("MainWindow", "Tesseract"))
        self.comboBoxScanner.setItemText(0, _translate("MainWindow", "Tesseract"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Choose the method that yields the best results.</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "OCR Method:"))
        self.label_3.setText(_translate("MainWindow", "Language:"))
        self.comboBoxLanguage.setCurrentText(_translate("MainWindow", "English"))
        self.comboBoxLanguage.setItemText(0, _translate("MainWindow", "English"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Scan"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Scanner"))
        self.pushButtonRestoreDefaults.setText(_translate("MainWindow", "Restore Defaults"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Developer"))
        self.checkBoxDebugMode.setToolTip(_translate("MainWindow", "Saves ALL screenshots"))
        self.checkBoxDebugMode.setText(_translate("MainWindow", "Debug mode"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Additional Delay (for slow computers)"))
        self.label_11.setToolTip(_translate("MainWindow", "<html><head/><body><p>Navigating between different pages</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Navigation speed (ms):"))
        self.label_13.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press between each individual achievement</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Scan speed (ms):"))
        self.spinBoxNavDelay.setPrefix(_translate("MainWindow", "+"))
        self.spinBoxScanDelay.setPrefix(_translate("MainWindow", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configure), _translate("MainWindow", "Configure"))
