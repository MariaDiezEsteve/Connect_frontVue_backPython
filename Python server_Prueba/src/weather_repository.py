import sqlite3


con = sqlite3.connect("weather.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE if not exists cities(id, name, temperature, rain_probability)")

def read_all():
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM cities")
    rows = res.fetchall()
    con.close()
    
    return rows


def read(city_id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM cities WHERE id=?", [city_id])
    row = res.fetchone()
    con.close()

    city = {"id": row[0],
            "name": row[1],
            "temperature": row[2],
            "rain_probability": row[3]
            }
    return city

def create(weather):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    res = "INSERT INTO cities VALUES(?, ?, ?, ?)"
    valores = (weather['id'], weather['name'],
               weather['temperature'], weather['rain_probability'])
    cur.execute(res, valores)
    con.commit()
    con.close()

def remove_city(id):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("DELETE FROM cities WHERE id=?", [id])
    con.commit()
    con.close()