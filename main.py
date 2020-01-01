import requests
from bs4 import BeautifulSoup
import sqlite3

# scraping craigslist - specify search terms, filter by 'new' in results, & saving results to slqlite db

def get_results():

    parameters = ['dildo', 'sofa', 'shoes' ]

    filtered_results = []

    for parameter in parameters:

        payload = {'query': parameter}

        url = "https://london.craigslist.org/search/sss"
        r = requests.get(url, params=payload)
        soup = BeautifulSoup(r.text, "lxml")
        results = soup.findAll('a', attrs={'class': 'result-title hdrlnk'})

        for result in results:
            if "new" in result.text.lower():
                filtered_results.append(result.text)

    return filtered_results

def create_db():
    try:
        sqliteConnection = sqlite3.connect('SQLite_SearchResults.db')

        create_table = '''CREATE TABLE IF NOT EXISTS Search_results (
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


# inserting multiple rows
def store_results(filtered_results):
    try:
        sqliteConnection = sqlite3.connect('SQLite_SearchResults.db')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")


        # can insert variable using ?
        update_table = '''INSERT INTO Search_results (result)
                                        VALUES
                                        (?);'''
        #breakpoint()

        for filtered_result in filtered_results:


            sqlite_select_query = """SELECT * FROM Search_results WHERE result = ?"""
            cursor.execute(sqlite_select_query, [filtered_result])
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))

            if len(records) == 0:

                cursor.execute(update_table, [filtered_result])
                # changing my items in a list into tuples!
                sqliteConnection.commit()
                print("Total", cursor.rowcount, "records inserted successfully into SQLite_SearchResults table ")


    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")



def main():
    results = get_results()
    create_db()
    store_results(results)

# tells python this file is being run as a script
if __name__ == '__main__':
    main()


