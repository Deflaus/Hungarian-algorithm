from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from munkres import Munkres
from sqll import DataBaseAccess
from tables import Table_1, Table_2, InputW, InputT


class FormActions():
    @staticmethod
    def StartMainTable():
        Form.show()
        FormActions.PrintMainTable()

    @staticmethod
    def PrintMainTable():
        table1.tableWidget.setColumnCount(DataBaseAccess.count_of_tasks())
        table1.tableWidget.setRowCount(DataBaseAccess.count_of_workers())
        table1.tableWidget.setHorizontalHeaderLabels(DataBaseAccess.get_names_of_tasks())
        table1.tableWidget.setVerticalHeaderLabels(DataBaseAccess.get_names_of_workers())

    @staticmethod
    def StartTableWorker():
        FormW.show()
        FormActions.PrintTableWork()

    @staticmethod
    def PrintTableWork():
        tableWork.tableWidget.setColumnCount(3)
        tableWork.tableWidget.setRowCount(DataBaseAccess.count_of_workers())
        listOfWork = ['ID', 'Имя', 'Должность']
        tableWork.tableWidget.setHorizontalHeaderLabels(listOfWork)
        data = DataBaseAccess.parse_alldata_workers()
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                element = QTableWidgetItem(str(col))
                element.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                tableWork.tableWidget.setItem(i, j, element)

    @staticmethod
    def StartTableTask():
        FormT.show()
        FormActions.PrintTableTask()

    @staticmethod
    def PrintTableTask():
        tableTask.tableWidget.setColumnCount(2)
        tableTask.tableWidget.setRowCount(DataBaseAccess.count_of_tasks())
        listOfTask = ['ID', 'Имя']
        tableTask.tableWidget.setHorizontalHeaderLabels(listOfTask)
        data = DataBaseAccess.parse_alldata_tasks()
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                element = QTableWidgetItem(str(col))
                element.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                tableTask.tableWidget.setItem(i, j, element)

    @staticmethod
    def btnAddWorker():
        FormInW.show()

    @staticmethod
    def btnDelWorker():
        DataBaseAccess.determine_id_worker(tableWork.tableWidget.currentRow())
        FormActions.PrintTableWork()

    @staticmethod
    def btnAddTask():
        FormInT.show()

    @staticmethod
    def btnDelTask():
        DataBaseAccess.determine_id_task(tableTask.tableWidget.currentRow())
        FormActions.PrintTableTask()

    @staticmethod
    def btnOkWorkerClicked():
        DataBaseAccess.insert_workers(inpW.lineEdit.text(), inpW.lineEdit_2.text(), inpW.lineEdit_3.text())
        FormActions.PrintTableWork()
        FormInW.close()

    @staticmethod
    def btnOkTaskClicked():
        DataBaseAccess.insert_tasks(inpT.lineEdit.text(), inpT.lineEdit_2.text())
        FormActions.PrintTableTask()
        FormInT.close()

    @staticmethod
    def ExportItemTable():
        FormActions.PrintMainTable()
        rows = DataBaseAccess.count_of_workers()
        cols = DataBaseAccess.count_of_tasks()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(table1.tableWidget.item(row, col).text())
                except:
                    tmp.append('Null')
            data.append(tmp)
        DataBaseAccess.insert_time(data)

    @staticmethod
    def SolveTask():
        try:
            table1.listWidget.clear()
            workers = DataBaseAccess.parse_alldata_workers()
            tasks = DataBaseAccess.parse_alldata_tasks()
            matrix = DataBaseAccess.get_time()
            m = Munkres()
            indexes = m.compute(matrix)
            total = 0
            for row, column in indexes:
                value = matrix[row][column]
                total += value
                item = QtWidgets.QListWidgetItem('Работник ' + str(workers[row][1]) + ' - ' + str(tasks[column][1]) + ' ( количество часов: ' + str(value) + ')')
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                table1.listWidget.addItem(item)
            item = QtWidgets.QListWidgetItem('Все время - ' + str(total) + ' часов')
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            table1.listWidget.addItem(item)
        except:
            item = QtWidgets.QListWidgetItem('Error')
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            table1.listWidget.addItem(item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    FormW = QtWidgets.QWidget()
    FormT = QtWidgets.QWidget()
    FormInW = QtWidgets.QWidget()
    FormInT = QtWidgets.QWidget()

    table1 = Table_1()
    tableWork = Table_2()
    tableTask = Table_2()
    inpW = InputW()
    inpT = InputT()

    table1.setupUi(Form)
    table1.pushButton_2.clicked.connect(FormActions.StartTableTask)
    table1.pushButton_3.clicked.connect(FormActions.StartTableWorker)
    table1.pushButton_4.clicked.connect(FormActions.ExportItemTable)
    table1.pushButton_5.clicked.connect(FormActions.SolveTask)

    tableWork.setupUi(FormW)
    tableWork.pushButton.clicked.connect(FormActions.btnAddWorker)
    tableWork.pushButton_2.clicked.connect(FormActions.btnDelWorker)

    tableTask.setupUi(FormT)
    tableTask.pushButton.clicked.connect(FormActions.btnAddTask)
    tableTask.pushButton_2.clicked.connect(FormActions.btnDelTask)

    inpW.setupUi(FormInW)
    inpW.pushButton.clicked.connect(FormActions.btnOkWorkerClicked)

    inpT.setupUi(FormInT)
    inpT.pushButton.clicked.connect(FormActions.btnOkTaskClicked)

    FormActions.StartMainTable()

    sys.exit(app.exec_())
