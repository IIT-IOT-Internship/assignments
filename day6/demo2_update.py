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
sensor_id = int(input("Enter sensor id whose moisture level to be updated: "))
moisture_lvl = int(input("Enter new moisture level: "))

# correct SQL query
query = "UPDATE field_information SET moisture_lvl = %s WHERE sensor_id = %s"

# create cursor
cursor = connection.cursor()

# execute query

moisture_lvl = float(input("Enter moisture level: "))
sensor_id = int(input("Enter sensor ID: "))
query = "UPDATE table SET col=%s WHERE id=%s"



# commit changes
connection.commit()

print("Moisture level updated successfully ✅")

# close resources
cursor.close()
connection.close()