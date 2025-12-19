import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture",
    use_pure=True
)

# take input
sensor_id = int(input("Enter sensor id: "))
moisture_lvl = int(input("Enter moisture level: "))
date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")

# parameterized query
query = """
INSERT INTO field_information (sensor_id, moisture_lvl, date_time)
VALUES (%s, %s, %s)
"""

# create cursor
cursor = connection.cursor()

# execute query
query = "INSERT INTO soil_moisture VALUES (%s, %s, %s)"


# commit changes
connection.commit()

print("Sensor data inserted successfully ✅")

# close cursor and connection
cursor.close()
connection.close()