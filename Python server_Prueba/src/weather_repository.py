import sqlite3


con = sqlite3.connect("weather.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE if not exists cities(id, name, temperature, rain_probability)")

def read_all():
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cities")
        rows = res.fetchall()
        
        #Opción 1: Para cambiar los valores de la lista en tuplas (objetos)
        city_list = []

        for row in rows:
            row = {"id": row[0],
                "name": row[1],
                "temperature": row[2],
                "rain_probability": row[3]
                }
            city_list.append(row)
            print("que es esto ", row)

        return city_list
    except:
        None
    finally:
        con.close()

     #Opción 2: Para cambiar los valores de la lista en tuplas (objetos)
    """
    columnas = ["id", "name", "temperature", "rain_probaility"]
    datos_dict[dict(zip(columnas, fila)) for fila in rows]
    return datos_dict
    """


def read(city_id):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM cities WHERE id=?", [city_id])
        row = res.fetchone()


        city = {"id": row[0],
                "name": row[1],
                "temperature": row[2],
                "rain_probability": row[3]
                }
        return city
    except:
        None
    finally:
        con.close()

def create(weather):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        res = "INSERT INTO cities VALUES(?, ?, ?, ?)"
        valores = (weather['id'], weather['name'],
                weather['temperature'], weather['rain_probability'])
        cur.execute(res, valores)
        con.commit()
    except:
        None
    finally:
        con.close()

def remove_city(id):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM cities WHERE id=?", [id])
        con.commit()
    except:
        None
    finally:
        con.close()

#Modificar

def update(new_id, new_name, new_temperature, new_rain_probability):
    con = sqlite3.connect("weather.db")
    try:
        cur = con.cursor()
        res = "UPDATE cities SET name = ?, temperature = ?, rain_probability = ? WHERE id = ?"
        values = (new_name, new_temperature, new_rain_probability, new_id)
        cur.execute(res, values)
        con.commit()
    except:
        None
    finally:
        con.close()

#Esta función sirve para incluir la data actualizada.

def update_city_data(city_id, data):
    new_name = data.get("name")
    new_temperature = data.get("temperature")
    new_rain_probability = data.get("rain_probability")
    
    update(city_id, new_name, new_temperature, new_rain_probability)
