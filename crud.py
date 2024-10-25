import mysql.connector

mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="testdataset")
mysqlcursor = mysqldb.cursor()
# create table
# mysqlcursor.execute("create table studentrecord(rollno INT, name VARCHAR(30), marks INT)")

# insert into table
'''
try:

    mysqlcursor.execute(
        "insert into studentrecord(roolno, name, marks) values(2, 'Prathik', 88)")
    mysqldb.commit()
    print("Record inserted into Table")
    mysqldb.close()
except:
    mysqldb.rollback()
mysqldb.close()
'''
'''
# display record
try:
    mysqlcursor.execute("select * from studentrecord")
    result = mysqlcursor.fetchall()
    for i in result:
        roll = i[0]
        name = i[1]
        marks = i[2]
        print(roll, name, marks)
except:
    print("some issue in code..")
mysqlcursor.close()
'''
# to update the record

# try:
#     mysqlcursor.execute(

#         "update studentrecord set name='Sachin', marks=88 where roolno=1 ")
#     mysqldb.commit()
#     print('Record updated')
# except:
#     mysqldb.rollback()
# mysqldb.close()

# delete the record
# try:
#     mysqlcursor.execute("delete from studentrecord where roolno=1 ")
#     mysqldb.commit()
#     print('Record deleted')
# except:
#     mysqldb.rollback()
# mysqldb.close()
