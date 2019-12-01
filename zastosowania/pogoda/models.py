import datetime
import sqlite3
from sqlite3 import Error

from pogoda import get_location_id, get_location_weather


def create_connection(db_file):
    """Tworzę połączenie z bazą"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn

create_table_sql ="""
CREATE TABLE IF NOT EXISTS weather (
  id integer PRIMARY KEY,
  location_name text NOT NULL,
  temperature integer NOT NULL, 
  date text NOT NULL
)
"""

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_weather(conn, weather, location_name):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = (location_name, weather.the_temp, now)
    sql = "INSERT INTO weather(location_name, temperature, date) VALUES (?,?,?);"
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

if __name__ == "__main__":
    conn = create_connection("test.db")
    # create_table(conn, create_table_sql)
    location_id = get_location_id("warsaw")
    weather = get_location_weather(location_id)
    print(create_weather(conn, weather, 'warsaw'))
    conn.close()


