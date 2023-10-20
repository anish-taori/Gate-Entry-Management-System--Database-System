import mysql.connector as my
import getpass
username = input("Enter mysql username:-")
password = input("Enter mysql password:-")
# username = "root"
# password = "yash2003"

mydb = my.connect(host="localhost", user=username,
                  password=password)

if mydb.is_connected():
    print("successfully connected")
else:
    print("Not connected")
# ----------------------------------------------------------------------------------------------------
# making gateway
mycon = mydb.cursor()
mycon.execute("drop database gateway")
mycon.execute("CREATE DATABASE gateway")
# mycon.execute("show databases")
# for i in mycon:
#     print(i)
# print()
mycon.execute("use gateway")
# ----------------------------------------------------------------------------------------------------
# creating table vehicle
mycon.execute("drop table if exists vehicle")
mycon.execute(
    "create table vehicle(license_plate_no varchar(15),vehicle_type varchar(5),primary key(license_plate_no))")
mydb.commit()
# mycon.execute("SHOW TABLES")
# for i in mycon:
#     print(i)

# creating table user
mycon.execute("drop table if exists user")
mycon.execute("create table user(user_id varchar(5),name varchar(20) not null,address varchar(20) not null,pincode varchar(10) not null,email varchar(20) not null,password varchar(20) not null,security_key varchar(10) not null, phone_no varchar(10) not null,primary key(user_id),unique key(email))")
mydb.commit()

# create table register
mycon.execute("drop table if exists register")
mycon.execute("create table registers(user_id varchar(5),license_plate_no varchar(15),primary key(license_plate_no),foreign key(user_id) references user(user_id)on delete cascade,foreign key(license_plate_no) references vehicle(license_plate_no)on delete cascade)")
mydb.commit()

# create table entry_exit_record
mycon.execute("drop table if exists entry_exit_record")
mycon.execute(
    "create table entry_exit_record(log_id varchar(5),entry_time time,exit_time time,primary key(log_id))")
mydb.commit()

# create table gate
mycon.execute("drop table if exists gate")
mycon.execute(
    "create table gate(gate_id varchar(5),location varchar(20) not null,primary key(gate_id))")
mydb.commit()

# create table gate_personnel
mycon.execute("drop table if exists gate_personnel")
mycon.execute("create table gate_personnel(gate_id varchar(5),personnel_id varchar(5) not null,primary key(personnel_id),foreign key (gate_id) references gate(gate_id)on delete cascade)")
mydb.commit()

# create table logs
mycon.execute("drop table if exists logs")
mycon.execute("create table logs(log_id varchar(5),license_plate_no varchar(15),gate_id varchar(5),primary key(log_id),foreign key (gate_id) references gate(gate_id)on delete cascade,foreign key (log_id) references entry_exit_record(log_id)on delete cascade,foreign key (license_plate_no) references vehicle(license_plate_no)on delete cascade)")
mydb.commit()

# create table can_access
mycon.execute("drop table if exists can_access")
mycon.execute("create table can_access(user_id varchar(5),gate_id varchar(5),primary key(user_id,gate_id),foreign key (user_id) references user(user_id)on delete cascade,foreign key (gate_id) references gate(gate_id)on delete cascade)")
mydb.commit()


# ----------------------------------------------------------------------------------------------------
# inserting values in all tables

# inserting values in user table
sql = "INSERT INTO user (user_id, name,address,pincode,email,password,security_key,phone_no) VALUES(%s, %s,%s, %s,%s, %s,%s,%s)"
val = [
    ('09390', 'Anish Taori', 'Chembur Mumbai', '400071',
     'anishtaori@gmail.com', 'pass09390', 'sharma', '8454071725'),
    ('02417', 'Yash Kandoi', 'Rajwada Siliguri', '400072',
     'yashkandoi@gmail.com', 'pass02417', 'verma', '9794784831'),
    ('08950', 'Prakhar Mundra', 'Vashi Mumbai', '400073',
     'prakhar@gmail.com', 'pass08950', 'sharma', '9454071725'),
    ('09260', 'Roshan Bagla', 'Ghatkopar Mumbai', '400074',
     'roshan@gmail.com', 'pass09260', 'verma', '8854071725'),
    ('02040', 'Aryan Seth', 'Andheri Mumbai', '400075',
     'aryan@gmail.com', 'pass02040', 'sharma', '8954071725'),
    ('07640', 'Sanju sanju', 'Dadar Mumbai', '400076',
     'sanju@gmail.com', 'pass07640', 'verma', '9454071725'),
    ('09340', 'Arush Dayal', 'Mahim Mumbai', '400077',
     'arush@gmail.com', 'pass09340', 'sharma', '9954071725'),
    ('04920', 'Hrishi kanodia', 'Varsova Mumbai', '400078',
     'hrishi@gmail.com', 'pass04920', 'verma', '9854071725'),
    ('01760', 'Afzal Aftab', 'Churchgate Mumbai', '400079',
     'afzal@gmail.com', 'pass01760', 'sharma', '8154071725'),
    ('01570', 'Amit Trivedi', 'Dadar Mumbai', '400080',
     'amit@gmail.com', 'pass01570', 'verma', '8054071725'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from user")
# for i in mycon:
#     print(i)
# print()

# inserting values in vehicle table

# license_plate_no = input("Enter license_plate_no :-")
# vehicle_type = input("Enter vehicle_type :-")
# mycon.execute("INSERT INTO student VALUES ('{}', '{}',)".format (license_plate_no, vehicle_type))

sql = "INSERT INTO vehicle (license_plate_no, vehicle_type) VALUES (%s, %s)"
val = [
    ('HR 26 DQ 5551', 'sedan'),
    ('HR 26 DQ 5458', 'sedan'),
    ('HR 26 DQ 5343', 'xuv'),
    ('MH 43 DQ 6291', 'suv'),
    ('MH 43 DQ 6343', 'xuv'),
    ('MH 43 DQ 6265', 'suv'),
    ('MH 43 DQ 6349', 'xuv'),
    ('HR 26 DQ 5291', 'suv'),
    ('HR 26 DQ 5581', 'sedan'),
    ('HR 26 DQ 9838', 'sedan'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from vehicle")
# for i in mycon:
#     print(i)
# print()


# inserting into registers table
sql = "INSERT INTO registers (user_id, license_plate_no) VALUES (%s, %s)"
val = [
    ('09390', 'HR 26 DQ 5458'),
    ('09390', 'HR 26 DQ 5551'),
    ('09390', 'HR 26 DQ 5581'),
    ('02417', 'HR 26 DQ 5343'),
    ('02417', 'HR 26 DQ 9838'),
    ('02417', 'MH 43 DQ 6291'),
    ('02417', 'MH 43 DQ 6343'),
    ('09390', 'HR 26 DQ 5291'),
    ('09390', 'MH 43 DQ 6265'),
    ('09390', 'MH 43 DQ 6349'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from registers")
# for i in mycon:
#     print(i)
# print()

# inserting into entry_exit_record table
sql = "INSERT INTO entry_exit_record (log_id, entry_time,exit_time) VALUES (%s, %s, %s)"
val = [
    (112, "13:9:36", "14:10:45"),
    (113, "13:19:36", "15:10:49"),
    (114, "14:9:36", "15:11:45"),
    (115, "11:9:36", "14:16:45"),
    (116, "11:19:36", "16:17:45"),
    (117, "10:9:36", "16:19:45"),
    (118, "13:19:36", "18:11:45"),
    (119, "15:9:36", "20:17:45"),
    (120, "19:19:36", "20:15:45"),
    (121, "15:9:36", "18:12:45"),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from entry_exit_record")
# for i in mycon:
#     print(i)
# print()

# inserting into gate table

sql = "INSERT INTO gate (gate_id, location) VALUES (%s, %s)"
val = [
    ('1', 'north1'),
    ('2', 'north2'),
    ('3', 'north3'),
    ('4', 'north4'),
    ('5', 'south1'),
    ('6', 'south2'),
    ('7', 'south3'),
    ('8', 'south4'),
    ('9', 'east1'),
    ('10', 'east2'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from gate")
# for i in mycon:
#     print(i)
# print()

# inserting into gate_personnel table
sql = "INSERT INTO gate_personnel (gate_id, personnel_id) VALUES (%s, %s)"
val = [
    ('1', '37'),
    ('1', '38'),
    ('1', '29'),
    ('1', '90'),
    ('1', '71'),
    ('1', '72'),
    ('2', '22'),
    ('2', '62'),
    ('2', '82'),
    ('2', '12'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from gate_personnel")
# for i in mycon:
#     print(i)
# print()

# inserting into logs table
sql = "INSERT INTO logs (log_id, license_plate_no,gate_id) VALUES (%s, %s, %s)"
val = [
    (112, 'HR 26 DQ 5458', '1'),
    (113, 'HR 26 DQ 5551', '1'),
    (114, 'HR 26 DQ 5581', '1'),
    (115, 'HR 26 DQ 5343', '1'),
    (116, 'HR 26 DQ 9838', '1'),
    (117, 'MH 43 DQ 6291', '2'),
    (118, 'MH 43 DQ 6343', '2'),
    (119, 'HR 26 DQ 5291', '2'),
    (120, 'MH 43 DQ 6265', '2'),
    (121, 'MH 43 DQ 6349', '2'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from logs")
# for i in mycon:
#     print(i)
# print()


# inserting into can_access table
sql = "INSERT INTO can_access (user_id, gate_id) VALUES (%s, %s)"
val = [
    ('09390', '1'),
    ('09390', '2'),
    ('09390', '3'),
    ('09390', '4'),
    ('09390', '5'),
    ('02417', '1'),
    ('02417', '2'),
    ('02417', '3'),
    ('02417', '4'),
    ('02417', '5'),
]

mycon.executemany(sql, val)
mydb.commit()

# mycon.execute("select * from can_access")
# for i in mycon:
#     print(i)
# print()

# ----------------------------------------------------------------------------------------------------

# Admin/user inputs
# authenticate
email1 = ''
password1 = ''
user_id2 = ''
name1 = ''
address1 = ''
pincode1 = ''
ph_number1 = ''
security_key1 = ''

print("Sample Login instructions:\n Email: anishtaori@gmail.com\n Password: pass09390 ")

while True:
    user_input = 0
    if user_input == 0:
        email1 = input("Enter email :-")
        password1 = input("Enter password :-")
        # password1=getpass.getpass('Password:')
        mycon.execute("SELECT user_id FROM user WHERE email = '%s' AND password = '%s'" % (
            email1, password1))
        user_id_result = -1
        for i in mycon:
            str = ''.join(i)
            user_id_result = str
            print(user_id_result)
        if int(user_id_result) == -1:
            print("Incorrect Login\n")
            continue
        user_id2 = user_id_result
        mycon.execute("SELECT email FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            email1 = str
        mycon.execute(
            "SELECT password FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            password1 = str
        mycon.execute("SELECT name FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            name1 = str
        mycon.execute(
            "SELECT address FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            address1 = str
        mycon.execute(
            "SELECT pincode FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            pincode1 = str
        mycon.execute(
            "SELECT phone_no FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            ph_number1 = str
        mycon.execute(
            "SELECT security_key FROM user WHERE user_id='%s'" % (user_id2))
        for i in mycon:
            str = ''.join(i)
            security_key1 = str
        print("Login successfull\n")
        print()
        print("Welcome to gateway management system.\n")
        # print(user_id2)
        # print(name1)
        # print(email1)
        # print(address1)
        # print(pincode1)
        # print(ph_number1)
        # print(security_key1)
        # print(password1)
        break


while True:

    # control menu
    user_input = input("\nPlease enter 0 to reset password.\nPlease enter 1 to add user. \n Please enter 2 to delete user.\n Please enter 3 to add gates.\n Please enter 13 to delete gates.\n Please enter 4 to log entry/exit time for vehicle.\nPlease enter 5 to register vehicle.\nPlease enter 6 to search vehicle records.\nPlease enter 7 to manage user profile.\nPlease enter 8 to find peak hours.\nPlease enter 9 to find vehicle types.\nPlease enter 10 to show gate utilization.\nPlease enter 11 to show vehicle logs.\n Please enter 12 to check authentication.\n Please enter 99 to exit.\nPlease enter your choice: ")
    user_input = int(user_input)

# reset password
    if user_input == 0:
        email = email1
        security_key = input("Enter security_key :-")
        mycon.execute("SELECT user_id FROM user WHERE email = '%s' AND security_key = '%s'" % (
            email, security_key))
        user_id_result = -1
        for i in mycon:
            str = ''.join(i)
            user_id_result = str
            print(user_id_result)
        if int(user_id_result) == -1:
            print("Incorrect Credentials\n")
            continue
        print("Correct Credentials\n")
        new_password = input("Enter new password :-")
        mycon.execute("UPDATE user SET password = '%s' WHERE user_id='%s'" % (
            new_password, user_id_result))
        mydb.commit()
        print("Password changed successfully")

# Please enter 12 to check authentication.
    if user_input == 12:
        email = input("Enter email :-")
        password = input("Enter password :-")
        mycon.execute("SELECT user_id FROM user WHERE email = '%s' AND password = '%s'" % (
            email, password))
        user_id_result = -1
        for i in mycon:
            str = ''.join(i)
            user_id_result = str
            print(user_id_result)
        if int(user_id_result) == -1:
            print("Incorrect Login\n")
        else:
            print("Login successfull\n")
        print()

# add user 1
    if user_input == 1:
        user_id = input("Enter user_id :-")
        name = input("Enter name :-")
        address = input("Enter address :-")
        pincode = input("Enter pincode :-")
        email = input("Enter email :-")
        password = input("Enter password :-")
        security_key = input("Enter security_key :-")
        phone_no = input("Enter phone_no :-")
        sql = "INSERT INTO user (user_id, name,address,pincode,email,password,security_key,phone_no) VALUES(%s, %s,%s, %s,%s, %s,%s, %s)"
        val = [
            (user_id, name, address, pincode, email,
             password, security_key, phone_no),
        ]

        mycon.executemany(sql, val)
        mydb.commit()
        print("User added\n")

# delete user 2
    elif user_input == 2:
        flag=0
        user_id1 = input("Enter user_id :-")
        mycon.execute("SELECT user_id FROM user")
        for i in mycon:
            str1=''.join(i)
            if str1==user_id1:
                flag=1
        if flag==1:
            mycon.execute("delete from user where user_id='%s'" % (user_id1))
            mydb.commit()
            print("Deleted User successfully")
        else:
            print("User not found")

# Add Gates 3
    elif user_input == 3:
        print("Sample input\n  gate_id :-11 , location :-pilani")
        gate_id = input("Enter gate_id :-")
        location = input("Enter location :-")
        sql = "INSERT INTO gate (gate_id, location) VALUES (%s, %s)"
        val = [
            (gate_id, location),
        ]
        mycon.executemany(sql, val)
        mydb.commit()
        print("Details update successfully")

# delete gates 13
    elif user_input == 13:
        flag=0
        gate_id = input("Enter gate_id :-")
        mycon.execute("select gate_id from gate")
        for i in mycon:
            str=''.join(i)
            if gate_id == str:
                flag=1
        if flag==1:
            mycon.execute("delete from gate where gate_id='%s'" % (gate_id))
            mydb.commit()
            print("Gate deleted successfully")
        else:
            print("Gate not found")

# Please enter 4 to log entry/exit time for vehicle.
    elif user_input == 4:
        print("Sample log:\n log_id :- 122,entry_time :- 13:9:36,exit_time :- 14:10:45,license_plate_no :- HR 26 DQ 5458,gate_id :- 10")
        log_id = input("Enter log_id :-")
        entry_time = input("Enter entry_time :-")
        exit_time = input("Enter exit_time :-")
        license_plate_no = input("Enter license_plate_no :-")
        gate_id = input("Enter gate_id :-")

        sql = "INSERT INTO entry_exit_record (log_id, entry_time,exit_time) VALUES (%s, %s, %s)"
        val = [
            (log_id, entry_time, exit_time),
        ]
        mycon.executemany(sql, val)
        mydb.commit()
        sql = "INSERT INTO logs (log_id, license_plate_no,gate_id) VALUES (%s, %s, %s)"
        val = [
            (log_id, license_plate_no, gate_id)
        ]
        mycon.executemany(sql, val)
        mydb.commit()

# Please enter 5 to add and register vehicle
    elif user_input == 5:
        print("Sample Input: license_plate_no:'HR 26 DQ 5551' ,vehicle_type:'sedan' ")
        mycon.execute("SELECT user_id FROM user WHERE email = '%s' AND password = '%s'" % (
            email1, password1))
        user_id_result = -1
        for i in mycon:
            str = ''.join(i)
            user_id_result = str
        # register vehicle
        license_plate_no = input("Enter license_plate_no :-")
        vehicle_type = input("Enter vehicle_type ('sedan','xuv','suv'):-")
        sql = "INSERT INTO vehicle (license_plate_no, vehicle_type) VALUES (%s, %s)"
        val = [
            (license_plate_no, vehicle_type),
        ]
        mycon.executemany(sql, val)
        mydb.commit()
        print("Vehicle successfully added\n")
        sql = "INSERT INTO registers (user_id, license_plate_no) VALUES (%s, %s)"
        val = [
            (user_id_result, license_plate_no),
        ]
        mycon.executemany(sql, val)
        mydb.commit()
        print("Vehicle successfully registered\n")

# Please enter 6 to search vehicle records based on filters.
    elif user_input == 6:
        menu_input = input(
            "Enter 0 to filter by name, 1 for phone number and 2 for pincode:-")
        if int(menu_input) == 0:
            mycon.execute(
                "select phone_no,name,license_plate_no from user natural join registers where name='%s'" % (name1))
            count = 0
            for i in mycon:
                print(i)
            print()

        if int(menu_input) == 1:
            mycon.execute(
                "select phone_no,name,license_plate_no from user natural join registers where phone_no='%s'" % (ph_number1))
            for i in mycon:
                print(i)
            print()
        if int(menu_input) == 2:
            mycon.execute(
                "select pincode,name,license_plate_no from user natural join registers where pincode='%s'" % (pincode1))
            for i in mycon:
                print(i)
            print()

# Please enter 7 to manage user profile.
    elif user_input == 7:
        new_no = input("Enter new ph number :-")
        new_add = input("Enter new address :-")
        new_pincode = input("Enter new pincode :-")
        new_email = input("Enter new email :-")
        mycon.execute("UPDATE user SET phone_no = '%s',address='%s',pincode='%s',email='%s' WHERE user_id='%s'" % (
            new_no, new_add, new_pincode, new_email, user_id2))
        mydb.commit()
        print("Changes executed successfully")


# Please enter 8 to find peak hours.
    elif user_input == 8:
        mycon.execute(
            "SELECT HOUR(entry_time) AS entry_hour, COUNT(*) AS entry_count FROM entry_exit_record GROUP BY entry_hour ORDER BY entry_count DESC LIMIT 1")
        for i in mycon:
            tuple = i
        print('Hour: %sth, Vehicle Count: %s' % tuple)
        print()

# Please enter 9 to find vehicle types.
    elif user_input == 9:
        mycon.execute(
            "SELECT vehicle_type, COUNT(*) AS count FROM vehicle natural join logs GROUP BY vehicle_type ORDER BY count DESC")
        for i in mycon:
            tuple = i
            print('Vehicle type: %s, Vehicle Count: %s' % tuple)
        print()

# Please enter 10 to show gate utilization.
    elif user_input == 10:
        mycon.execute(
            "SELECT gate_id, COUNT(*) AS count FROM gate natural join logs GROUP BY gate_id ORDER BY count DESC")
        for i in mycon:
            tuple = i
            print('Gate ID: %s, Vehicle Count: %s' % tuple)
        print()

# Please enter 11 to show vehicle logs.
    elif user_input == 11:
        mycon.execute(
            "select name,license_plate_no,gate_id,entry_time,exit_time from (user natural join (registers natural join logs)) natural join entry_exit_record where name='%s'" % (name1))
        for i in mycon:
            # print(i)
            tuple = i
            print(
                'Name: %s, License plate no: %s, GateID: %s, Entry Time: %s, Exit time: %s ' % tuple)
        print()

# Please enter 99 to exit
    elif user_input == 99:
        print("Exit application")
        break
    else:
        print("Wrong choice. Choose again")


# ----------------------------------------------------------------------------------------------------
# closing database
mydb.close()
