import sqlite3
from sqlite3 import Error
import pandas as pd
import os



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def checkForDevice():

    dbFile = "RaMBLE-test1.sqlite"

    if os.path.isfile(dbFile):
        print ("File exist")

        try:
            # Read sqlite query results into a pandas DataFrame
            con = sqlite3.connect(dbFile)
            cursorObj = con.cursor()
            cursorObj.execute('SELECT name from sqlite_master where type= "table"')


            print("Tables in loaded file: ", cursorObj.fetchall())
            df = pd.read_sql_query("SELECT * from devices", con)

            # Verify that result of SQL query is stored in the dataframe
            print(df.columns)

            deviceOccurances = df.loc[df['device_name'] == "JamppaMini"]

            print(deviceOccurances)

            if deviceOccurances.empty:
                return False
            else:
                return True

            con.close()

        except:
            return False
    else:
        print ("File not exist")
        return False





if __name__ == '__main__':
    checkForDevice()
