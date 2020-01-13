import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='root',database='Demo',)

run = conn.cursor()
run.execute("select * from Employee")
Employee_Details = run.fetchall()
for record in Employee_Details:
	print(record)
