import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

# correct SQL query
query = "SELECT * FROM sensor_readings"

# create cursor
cursor = connection.cursor()

# execute query
cursor.execute(query, (sensor_id, moisture_lvl, date_time))


# fetch all records
records = cursor.fetchall()

# print records
for record in records:
    print(record)

# close cursor and connection
cursor.close()
connection.close()