import sqlite3


class DataBaseAccess:
    @staticmethod
    def insert_tasks(id, task):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("INSERT INTO tasks VALUES(" + id + ',"' + task + '") ')
            con.commit()

            cur.close()
            con.close()
        except:
            pass

    @staticmethod
    def delete_task(id):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute('DELETE FROM tasks WHERE ID = "' + id + '" ')
            con.commit()

            cur.close()
            con.close()
        except:
            pass

    @staticmethod
    def update_task(id, task):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute(
                'UPDATE tasks SET Task = "' + task + '" WHERE ID = "' + str(id) + '" '
            )
            con.commit()

            cur.close()
            con.close()
        except:
            pass

    @staticmethod
    def parse_alldata_tasks():
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM tasks")

            data = cur.fetchall()

            cur.close()
            con.close()

            return data
        except:
            return []

    @staticmethod
    def count_of_tasks():
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("SELECT COUNT(*) FROM tasks")
            data = cur.fetchall()

            cur.close()
            con.close()

            return data[0][0]
        except:
            return 0

    @staticmethod
    def get_names_of_tasks():
        names_of_columns = []
        tasks = DataBaseAccess.parse_alldata_tasks()
        for row in tasks:
            names_of_columns.append(row[1])
        return names_of_columns

    @staticmethod
    def determine_id_task(currentRow):
        data = DataBaseAccess.parse_alldata_tasks()
        DataBaseAccess.delete_task(str(data[currentRow][0]))

    # WORKERS ACCESS

    @staticmethod
    def insert_workers(id, name, position):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute(
                "INSERT INTO workers VALUES("
                + id
                + ',"'
                + name
                + '","'
                + position
                + '") '
            )
            con.commit()

            cur.close()
            con.close()
        except:
            pass

    @staticmethod
    def delete_worker(id):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute('DELETE FROM workers WHERE ID = "' + id + '" ')
            con.commit()

            con.commit()

            cur.close()
            con.close()
        except:
            pass

    @staticmethod
    def update_worker(id, name, position):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute(
                'UPDATE workers SET Name = "'
                + name
                + '", Position = "'
                + position
                + '" WHERE ID = "'
                + str(id)
                + '" '
            )
            con.commit()

            cur.close()
            con.close()
        except:
            pass

    @staticmethod
    def parse_alldata_workers():
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM workers")

            data = cur.fetchall()

            cur.close()
            con.close()

            return data
        except:
            return []

    @staticmethod
    def count_of_workers():
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("SELECT COUNT(*) FROM workers")
            data = cur.fetchall()

            cur.close()
            con.close()
            return data[0][0]
        except:
            return 0

    @staticmethod
    def get_names_of_workers():
        names_of_rows = []
        tasks = DataBaseAccess.parse_alldata_workers()
        for row in tasks:
            names_of_rows.append(row[1])
        return names_of_rows

    @staticmethod
    def determine_id_worker(currentRow):
        data = DataBaseAccess.parse_alldata_workers()
        DataBaseAccess.delete_worker(str(data[currentRow][0]))

    # TIME ACCESS

    @staticmethod
    def parse_alldata_time():
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM time")

            data = cur.fetchall()

            cur.close()
            con.close()

            return data
        except:
            pass

    @staticmethod
    def parse_data_time(id):
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("SELECT Time FROM time WHERE IDoW = " + str(id))

            data = cur.fetchall()

            cur.close()
            con.close()

            return data
        except:
            pass

    @staticmethod
    def get_time():
        workers_table = DataBaseAccess.parse_alldata_workers()
        tasks_table = DataBaseAccess.parse_alldata_tasks()
        time = []

        for rowsW in workers_table:
            countC = 0
            ti = []
            for rowsT in tasks_table:
                if countC == len(tasks_table):
                    continue
                tasks = DataBaseAccess.parse_data_time(rowsW[0])
                for j in tasks:
                    for i in j:
                        ti.append(i)
                        countC += 1
            time.append(ti)
        return time

    @staticmethod
    def insert_time(data):

        tasks = DataBaseAccess.parse_alldata_tasks()
        workers = DataBaseAccess.parse_alldata_workers()
        try:
            con = sqlite3.connect("ss.db")
            cur = con.cursor()

            cur.execute("DELETE FROM time")

            for i, worker in enumerate(workers):
                for j, task in enumerate(tasks):
                    cur.execute(
                        "INSERT INTO time VALUES("
                        + str(worker[0])
                        + ","
                        + str(task[0])
                        + ","
                        + str(data[i][j])
                        + ") "
                    )
                    con.commit()

            cur.close()
            con.close()
        except:
            pass
