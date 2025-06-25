import mysql.connector


def execute_query(query):
    connection = mysql.connector.connect(
        port = 3306, user="root",host= 'localhost', password="Kautilya@123", database = "FitTrack"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

def execute_select_query(query):
    connection = mysql.connector.connect(
        port = 3306, user="root",host= 'localhost', password="Kautilya@123", database = "FitTrack"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    data= cursor.fetchall()
    cursor.close()
    connection.close()
    return data