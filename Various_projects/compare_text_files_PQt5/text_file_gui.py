from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Various_projects.compare_text_files_PQt5 import compare_files_gui


class Ui_Dialog(object):

    # method that reads first text file
    def read_first_file(self):
        global first_file_data
        first_file_data = []
        first_file = compare_files_gui.file_path()
        with open(first_file, 'r') as first_file:
            first_file_data = first_file.read()
        self.first_status_lbl.setText("First file loaded!")
        return first_file_data

    # method that reads second text file
    def read_second_file(self):
        global second_file_data
        second_file = compare_files_gui.file_path()
        with open(second_file, 'r') as second_file:
            second_file_data = second_file.read()
        self.second_status_lbl.setText("Second file loaded!")
        return second_file_data

    # method that finds different lines between both files
    def process_files(self):
        global difference_set
        difference_set = compare_files_gui.find_differences(first_file_data.split('\n'), second_file_data.split('\n'))
        Ui_Dialog.file_save(self)

    # method to save differences in other file and save in txt file
    def file_save(self):
        save_file, _ = QFileDialog.getSaveFileName()
        save_name = save_file + '.txt'
        with open(save_name, 'w') as save_file:
            for line in difference_set:
                save_file.write(line + '\n')
        self.first_status_lbl_3.setText("Finished!")

    # exit application method
    def exit_application(self):
        sys.exit(app.exec_())

    def setupUi(self, Dialog):
        # create non-modal window
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 400)
        Dialog.setMinimumSize(QtCore.QSize(480, 400))
        Dialog.setMaximumSize(QtCore.QSize(480, 400))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)

        # create frames
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(9, 9, 461, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #create labels
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 0, 181, 16))

        # set-up fonts
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        # others
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)

        # create lines
        self.line.setGeometry(QtCore.QRect(0, 20, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 130, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 290, 461, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        # create buttons
        self.exit_button = QtWidgets.QPushButton(self.frame)
        self.exit_button.setGeometry(QtCore.QRect(360, 330, 101, 41))
        self.exit_button.setObjectName("exit_button")

        # create lines
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(0, 210, 461, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        # create labels
        self.first_label = QtWidgets.QLabel(self.frame)
        self.first_label.setGeometry(QtCore.QRect(0, 60, 461, 16))
        self.first_label.setObjectName("first_label")
        self.second_label = QtWidgets.QLabel(self.frame)
        self.second_label.setGeometry(QtCore.QRect(0, 140, 461, 16))
        self.second_label.setObjectName("second_label")

        # create buttons
        self.first_file_load_btn = QtWidgets.QPushButton(self.frame)
        self.first_file_load_btn.setGeometry(QtCore.QRect(150, 80, 141, 41))
        self.first_file_load_btn.setObjectName("first_file_load_btn")
        self.second_file_load_btn = QtWidgets.QPushButton(self.frame)
        self.second_file_load_btn.setGeometry(QtCore.QRect(150, 160, 141, 41))
        self.second_file_load_btn.setObjectName("second_file_load_btn")

        # create lines
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 40, 461, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        #create lables
        self.info_label = QtWidgets.QLabel(self.frame)
        self.info_label.setGeometry(QtCore.QRect(10, 30, 461, 16))
        self.info_label.setTextFormat(QtCore.Qt.RichText)
        self.info_label.setObjectName("info_label")

        # create line
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(0, 50, 461, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        # create label
        self.third_label = QtWidgets.QLabel(self.frame)
        self.third_label.setGeometry(QtCore.QRect(0, 220, 461, 16))
        self.third_label.setObjectName("third_label")

        # create third button
        self.process_and_save_btn = QtWidgets.QPushButton(self.frame)
        self.process_and_save_btn.setGeometry(QtCore.QRect(150, 240, 141, 41))

        # create status labels
        self.process_and_save_btn.setObjectName("process_and_save_btn")
        self.first_status_lbl = QtWidgets.QLabel(self.frame)
        self.first_status_lbl.setGeometry(QtCore.QRect(330, 90, 100, 21))
        self.first_status_lbl.setObjectName("first_status_lbl")
        self.second_status_lbl = QtWidgets.QLabel(self.frame)
        self.second_status_lbl.setGeometry(QtCore.QRect(330, 170, 100, 21))
        self.second_status_lbl.setObjectName("first_status_lbl_2")
        self.first_status_lbl_3 = QtWidgets.QLabel(Dialog)
        self.first_status_lbl_3.setGeometry(QtCore.QRect(210, 320, 100, 21))
        self.first_status_lbl_3.setObjectName("first_status_lbl_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Text file compare application"))
        self.label.setText(_translate("Dialog", "Compare text files"))
        self.exit_button.setText(_translate("Dialog", "Quit"))
        self.first_label.setText(_translate("Dialog", "1) Load first text file to compare"))
        self.second_label.setText(_translate("Dialog", "2) Load second text file to compare"))
        self.first_file_load_btn.setText(_translate("Dialog", "Load first file"))
        self.second_file_load_btn.setText(_translate("Dialog", "Load second file"))
        self.info_label.setText(_translate("Dialog", "Application compares two .TXT files (line by line) and saves differences in separate file."))
        self.third_label.setText(_translate("Dialog", "3) Process files and save output file"))
        self.process_and_save_btn.setText(_translate("Dialog", "Process files"))
        self.first_status_lbl.setText(_translate("Dialog", " "))
        self.second_status_lbl.setText(_translate("Dialog", " "))
        self.first_status_lbl_3.setText(_translate("Dialog", " "))

        # calling methods in GUI
        self.exit_button.clicked.connect(self.exit_application)
        self.first_file_load_btn.clicked.connect(self.read_first_file)
        self.second_file_load_btn.clicked.connect(self.read_second_file)
        self.process_and_save_btn.clicked.connect(self.process_files)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())