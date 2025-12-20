import mysql.connector
from datetime import datetime

# ================= DATABASE CONNECTION BLOCK =================
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agriculture"
)
cur = con.cursor()

# ================= CREATE BLOCK =================
def insert_record():
    sid = int(input("Enter Sensor ID: "))
    moisture = float(input("Enter Moisture Level: "))
    dt = datetime.now()

    cur.execute(
        "INSERT INTO soil_moisture VALUES (%s, %s, %s)",
        (sid, moisture, dt)
    )
    con.commit()
    print("Record Inserted Successfully")

# ================= READ BLOCK =================
def display_all():
    cur.execute("SELECT * FROM soil_moisture")
    rows = cur.fetchall()

    if not rows:
        print("No records found")
    else:
        for row in rows:
            print(row)

# ================= UPDATE BLOCK =================
def update_record():
    sid = int(input("Enter Sensor ID to update: "))
    moisture = float(input("Enter new moisture level: "))

    cur.execute(
        "UPDATE soil_moisture SET moisture_level = %s WHERE sensor_id = %s",
        (moisture, sid)
    )
    con.commit()
    print("Record Updated Successfully")

# ================= DELETE BLOCK =================
def delete_record():
    sid = int(input("Enter Sensor ID to delete: "))

    cur.execute(1
            
        "DELETE FROM soil_moisture WHERE sensor_id = %s",
        (sid,)
    )
    con.commit()
    print("Record Deleted Successfully")

# ================= YESTERDAY RECORDS BLOCK =================
def yesterday_records():
    cur.execute("""
        SELECT * FROM soil_moisture
        WHERE DATE(date_time) = CURDATE() - INTERVAL 1 DAY
    """)
    rows = cur.fetchall()

    if not rows:
        print("No records from yesterday")
    else:
        for row in rows:
            print(row)

# ================= BELOW THRESHOLD BLOCK =================
def below_threshold():
    t = float(input("Enter threshold value: "))

    cur.execute(
        "SELECT * FROM soil_moisture WHERE moisture_level < %s",
        (t,)
    )
    rows = cur.fetchall()

    if not rows:
        print("No records below threshold")
    else:
        for row in rows:
            print(row)

# ================= MENU BLOCK =================
while True:
    print("\n--- SMART AGRICULTURE MENU ---")
    print("1. Insert Record")
    print("2. Display Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Yesterday Records")
    print("6. Below Threshold")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        insert_record()
    elif ch == 2:
        display_all()
    elif ch == 3:
        update_record()
    elif ch == 4:
        delete_record()
    elif ch == 5:
        yesterday_records()
    elif ch == 6:
        below_threshold()
    elif ch == 7:
        print("Program Terminated")
        break
    else:
        print("Invalid Choice")

# ================= CLOSE CONNECTION BLOCK =================
cur.close()
con.close()
