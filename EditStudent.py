from PyQt5 import QtCore, QtGui, QtWidgets
import icons

class Ui_EditStudentForm(object):
    def setupUi(self, EditStudentForm):
        EditStudentForm.setObjectName("EditStudentForm")
        EditStudentForm.resize(300, 328)
        EditStudentForm.setMinimumSize(QtCore.QSize(300, 328))
        EditStudentForm.setMaximumSize(QtCore.QSize(300, 328))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditStudentForm.setWindowIcon(icon)
        self.EditStudentTabSwitcher = QtWidgets.QTabWidget(EditStudentForm)
        self.EditStudentTabSwitcher.setGeometry(QtCore.QRect(0, 0, 331, 351))
        self.EditStudentTabSwitcher.setObjectName("EditStudentTabSwitcher")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.CancelButton2 = QtWidgets.QPushButton(self.tab)
        self.CancelButton2.setGeometry(QtCore.QRect(210, 260, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.CancelButton2.setFont(font)
        self.CancelButton2.setObjectName("CancelButton2")
        self.NextButton = QtWidgets.QPushButton(self.tab)
        self.NextButton.setGeometry(QtCore.QRect(130, 260, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.NextButton.setFont(font)
        self.NextButton.setObjectName("NextButton")
        self.NameInput = QtWidgets.QLineEdit(self.tab)
        self.NameInput.setGeometry(QtCore.QRect(130, 70, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.NameInput.setFont(font)
        self.NameInput.setObjectName("NameInput")
        self.NameLabel = QtWidgets.QLabel(self.tab)
        self.NameLabel.setGeometry(QtCore.QRect(20, 70, 50, 15))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 75, 15))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 50, 15))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.DepartmentComboBox = QtWidgets.QComboBox(self.tab)
        self.DepartmentComboBox.setGeometry(QtCore.QRect(130, 160, 151, 22))
        self.DepartmentComboBox.setObjectName("DepartmentComboBox")
        self.DepartmentComboBox.addItem("")
        self.DepartmentComboBox.addItem("")
        self.DepartmentComboBox.addItem("")
        self.DepartmentComboBox.addItem("")
        self.DepartmentComboBox.addItem("")
        self.YearComboBox = QtWidgets.QComboBox(self.tab)
        self.YearComboBox.setGeometry(QtCore.QRect(220, 130, 60, 20))
        self.YearComboBox.setObjectName("YearComboBox")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.PhoneInput = QtWidgets.QLineEdit(self.tab)
        self.PhoneInput.setGeometry(QtCore.QRect(130, 190, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.PhoneInput.setFont(font)
        self.PhoneInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PhoneInput.setObjectName("PhoneInput")
        self.AddressInput = QtWidgets.QLineEdit(self.tab)
        self.AddressInput.setGeometry(QtCore.QRect(130, 220, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.AddressInput.setFont(font)
        self.AddressInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.AddressInput.setObjectName("AddressInput")
        self.GenderComboBox = QtWidgets.QComboBox(self.tab)
        self.GenderComboBox.setGeometry(QtCore.QRect(220, 100, 60, 20))
        self.GenderComboBox.setObjectName("GenderComboBox")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(20, 100, 50, 15))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.SearchInputForEdit = QtWidgets.QLineEdit(self.tab)
        self.SearchInputForEdit.setGeometry(QtCore.QRect(20, 20, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.SearchInputForEdit.setFont(font)
        self.SearchInputForEdit.setObjectName("SearchInputForEdit")
        self.SearchButtonForEdit = QtWidgets.QPushButton(self.tab)
        self.SearchButtonForEdit.setGeometry(QtCore.QRect(210, 20, 70, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.SearchButtonForEdit.setFont(font)
        self.SearchButtonForEdit.setObjectName("SearchButtonForEdit")
        self.EditStudentTabSwitcher.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.CancelButton = QtWidgets.QPushButton(self.tab_2)
        self.CancelButton.setGeometry(QtCore.QRect(210, 260, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CancelButton.setFont(font)
        self.CancelButton.setObjectName("CancelButton")
        self.AddStudentButton = QtWidgets.QPushButton(self.tab_2)
        self.AddStudentButton.setGeometry(QtCore.QRect(130, 260, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.AddStudentButton.setFont(font)
        self.AddStudentButton.setObjectName("AddStudentButton")
        self.BackButton = QtWidgets.QPushButton(self.tab_2)
        self.BackButton.setGeometry(QtCore.QRect(50, 260, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 110, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 140, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 170, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 200, 200, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.MathInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.MathInput.setGeometry(QtCore.QRect(220, 20, 62, 22))
        self.MathInput.setObjectName("MathInput")
        self.DSInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.DSInput.setGeometry(QtCore.QRect(220, 50, 62, 22))
        self.DSInput.setObjectName("DSInput")
        self.ISInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.ISInput.setGeometry(QtCore.QRect(220, 80, 62, 22))
        self.ISInput.setObjectName("ISInput")
        self.OOPInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.OOPInput.setGeometry(QtCore.QRect(220, 110, 62, 22))
        self.OOPInput.setObjectName("OOPInput")
        self.PMInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.PMInput.setGeometry(QtCore.QRect(220, 140, 62, 22))
        self.PMInput.setObjectName("PMInput")
        self.BAInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.BAInput.setGeometry(QtCore.QRect(220, 170, 62, 22))
        self.BAInput.setObjectName("BAInput")
        self.TWInput = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.TWInput.setGeometry(QtCore.QRect(220, 200, 62, 22))
        self.TWInput.setObjectName("TWInput")
        self.EditStudentTabSwitcher.addTab(self.tab_2, "")

        self.retranslateUi(EditStudentForm)
        self.EditStudentTabSwitcher.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EditStudentForm)

    def retranslateUi(self, EditStudentForm):
        _translate = QtCore.QCoreApplication.translate
        EditStudentForm.setWindowTitle(_translate("EditStudentForm", "Edit Student"))
        self.CancelButton2.setText(_translate("EditStudentForm", "Cancel"))
        self.NextButton.setText(_translate("EditStudentForm", "Next"))
        self.NameLabel.setText(_translate("EditStudentForm", "Name"))
        self.label_2.setText(_translate("EditStudentForm", "Department"))
        self.label_3.setText(_translate("EditStudentForm", "Year"))
        self.label_4.setText(_translate("EditStudentForm", "Phone Number"))
        self.label_5.setText(_translate("EditStudentForm", "Address"))
        self.DepartmentComboBox.setItemText(0, _translate("EditStudentForm", "Computer system"))
        self.DepartmentComboBox.setItemText(1, _translate("EditStudentForm", "Information Technology"))
        self.DepartmentComboBox.setItemText(2, _translate("EditStudentForm", "Information systems"))
        self.DepartmentComboBox.setItemText(3, _translate("EditStudentForm", "Software Engineering"))
        self.DepartmentComboBox.setItemText(4, _translate("EditStudentForm", "Bio-Informatics"))
        self.YearComboBox.setItemText(0, _translate("EditStudentForm", "1"))
        self.YearComboBox.setItemText(1, _translate("EditStudentForm", "2"))
        self.YearComboBox.setItemText(2, _translate("EditStudentForm", "3"))
        self.YearComboBox.setItemText(3, _translate("EditStudentForm", "4"))
        self.GenderComboBox.setItemText(0, _translate("EditStudentForm", "Male"))
        self.GenderComboBox.setItemText(1, _translate("EditStudentForm", "Female"))
        self.label_13.setText(_translate("EditStudentForm", "Gender"))
        self.SearchInputForEdit.setPlaceholderText(_translate("EditStudentForm", "ID"))
        self.SearchButtonForEdit.setText(_translate("EditStudentForm", "Search"))
        self.EditStudentTabSwitcher.setTabText(self.EditStudentTabSwitcher.indexOf(self.tab), _translate("EditStudentForm", "Student Details"))
        self.CancelButton.setText(_translate("EditStudentForm", "Cancel"))
        self.AddStudentButton.setText(_translate("EditStudentForm", "Finish"))
        self.BackButton.setText(_translate("EditStudentForm", "Back"))
        self.label_6.setText(_translate("EditStudentForm", "Maths Grade"))
        self.label_7.setText(_translate("EditStudentForm", "Discreet Structers Grade"))
        self.label_8.setText(_translate("EditStudentForm", "Information System Grade"))
        self.label_9.setText(_translate("EditStudentForm", "Object Oriented Programming"))
        self.label_10.setText(_translate("EditStudentForm", "Project Management Grade"))
        self.label_11.setText(_translate("EditStudentForm", "Buissness administration Grade"))
        self.label_12.setText(_translate("EditStudentForm", "Technical Writing Grade"))
        self.EditStudentTabSwitcher.setTabText(self.EditStudentTabSwitcher.indexOf(self.tab_2), _translate("EditStudentForm", "Student Grades"))