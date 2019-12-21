import sqlite3

# working out how to create my db etc IGNORE THIS

try:
    sqliteConnection = sqlite3.connect('SQLite_SearchResults.db')

    create_table = '''CREATE TABLE Search_results (
                                    id INTEGER PRIMARY KEY,
                                    result TEXT NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(create_table)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")