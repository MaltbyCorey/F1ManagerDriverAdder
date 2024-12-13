import sqlite3


def add_basic_data(staff_id, first_name, last_name, country_id, dob, dob_iso, gender, is_generated_staff, photo_day,
                   face_type, face_index, age_type, is_generated_for_custom_team):
    main_db = sqlite3.connect('result/main.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = (
        "INSERT INTO Staff_BasicData (StaffID,FirstName,LastName,CountryID,DOB,DOB_ISO,Gender,IsGeneratedStaff"
        "PhotoDay,FaceType,FaceIndex,AgeType,IsGeneratedForCustomTeam) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)")
    try:
        cursor.execute(sql_query, (staff_id, first_name, last_name, int(country_id), int(dob), dob_iso,
                                   int(gender), int(is_generated_staff), int(photo_day), int(face_type),
                                   int(face_index),
                                   int(age_type), int(is_generated_for_custom_team)))
    except:
        print("StaffID already exists")
    else:
        main_db.commit()
        print("Successfully added staff")
    finally:
        main_db.close()
        print("Database closed")


def main():
    # Getting data from drivers db
    drivers_db = sqlite3.connect('drivers.db')

    # Staff_BasicData retrieval
    basic_data = []
    cursor = drivers_db.cursor()
    sql_query = "SELECT * FROM Staff_BasicData"
    cursor.execute(sql_query)
    all_basic_rows = cursor.fetchall()
    for row in all_basic_rows:
        staff_id = row[0]
        first_name = row[1]
        last_name = row[2]
        country_id = row[3]
        dob = row[4]
        dob_iso = row[5]
        gender = row[6]
        is_generated_staff = row[7]
        photo_day = row[8]
        face_type = row[9]
        face_index = row[10]
        age_type = row[11]
        is_generated_for_custom_team = row[12]
        add_basic_data(staff_id, first_name, last_name, country_id, dob, dob_iso, gender, is_generated_staff,
                       photo_day, face_type, face_index, age_type, is_generated_for_custom_team)

    sql_query = "SELECT * FROM Staff_GameData"
    game_data_out = drivers_db.execute(sql_query).fetchall()
    sql_query = "SELECT * FROM Staff_DriverData"
    driver_data_out = drivers_db.execute(sql_query).fetchall()
    sql_query = "SELECT * FROM Staff_PerformanceStats"
    performance_stats_out = drivers_db.execute(sql_query).fetchall()
    sql_query = "SELECT * FROM Staff_State"
    state_out = drivers_db.execute(sql_query).fetchall()
    drivers_db.close()


if __name__ == '__main__':
    main()
