import mysql.connector
import random
import pandas as pd
import csv
import pymysql
import threading
import time

l=[500,1000,1500,2000,2500]
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="alaskayoung",
database="MYDB"
)

#CASE1

df1 = pd.DataFrame()
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student(id INT PRIMARY KEY, name VARCHAR(255), age INT, address VARCHAR(255), gender CHAR);")
query = " create table studentc1 as select * from student where 1=2;"
mycursor.execute(query)
for j in range(len(l)):
    for i in range(0,l[j]):
        query = "insert into student values(" + str(i) + ',' + " 'name" + str(i) + "'," + str(random.randint(3, 20)) + ',' + ' "Delhi" ' + ',' + ' 0 ' ");"
        mycursor.execute(query)
     mydb.commit()
     start=time.time()
     query="INSERT INTO studentc1 (id,name, age, address,gender) SELECT id,upper(name), age+1, upper(address),not gender FROM student"
     mycursor.execute(query)
     mydb.commit()
     end=time.time()
     diff1=end-start
     df1.loc[j, 0] = diff1
     mycursor.execute("set sql_safe_updates=0;")
     mycursor.execute("delete from student where 1=1;")
     mycursor.execute("delete from studentc1 where 1=1;")
     mydb.commit()
df1.to_csv('analysis.csv', index=False)


#case 2

df=pd.read_csv("analysis.csv")
conn = pymysql.connect(host="localhost", user='root', password='alaskayoung', database='MYDB')
cursor = conn.cursor()
cursor.execute("CREATE TABLE student(id INT PRIMARY KEY, name VARCHAR(255), age INT, address VARCHAR(255), gender CHAR);")
query = " create table studentc2 as select * from student where 1=2; "
cursor.execute(query)
for j in range(len(l)):
     for i in range(0,l[j]):
        query = "insert into student values(" + str(i) + ',' + " 'name" + str(i) + "'," + str(random.randint(3, 20)) + ',' + ' "Delhi" ' + ',' + ' 0 ' ");"
        cursor.execute(query)
     mydb.commit()
     start=time.time()
     query = 'select * from student'
     results = pd.read_sql_query(query, conn)
     results.to_csv("output.csv", index=False)
     data = pd.read_csv("output.csv")
     data["name"] = data["name"].str.upper()
     data["age"] = data["age"]+1
     data["address"] = data["address"].str.upper()
     data['gender'] = data['gender'].map({0:1,1: 0})
     data.to_csv("output.csv", index=False)
     df1 = pd.DataFrame(data, columns= ["id","name","age", "address","gender"])
     for row in df1.itertuples():
        query1 ="insert into studentc2 values(" + str(row.id) + ',' + '"' + str(row.name) + '"' + ',' + str(row.age) + ',' + '"' + str(row.address) + '"' + ',' + str(row.gender) + ");"
        cursor.execute(query1)
     conn.commit()
     end=time.time()
     diff1=end-start
     df.loc[j, 1] = diff1
     cursor.execute("delete from student where 1=1;")
     cursor.execute("delete from studentc2 where 1=1;")
df.to_csv('analysis.csv', index=False)

case3
df=pd.read_csv("analysis.csv")
conn = pymysql.connect(host="localhost", user='root', password='alaskayoung', database='MYDB')
cursor = conn.cursor()
def extract(x,j):
   if(x<j):
       query = 'select * from student limit ' + str(x) + ', ' + str(int(j/5)) + ';'
        results = pd.read_sql_query(query, conn)
        results.to_csv("output" + str(x) + ".csv", index=False)
        t2 = threading.Thread(target=transform, args=("output" + str(x) + ".csv",))
        t2.start()
        t2.join()
        extract(x+10,j)

def transform(file):
    data = pd.read_csv(file)
    data["name"] = data["name"].str.upper()
    data["age"] = data["age"]+1
   data["address"] = data["address"].str.upper()
    data['gender'] = data['gender'].map({0:1,1: 0})
    data.to_csv(file, index=False)
    load(file)

def load(file):
   data = pd.read_csv(file)
    df = pd.DataFrame(data, columns= ["id","name","age", "address","gender"])
    for row in df.itertuples():
        query1 ="insert into studentc3 values(" + str(row.id) + ',' + '"' + str(row.name) + '"' + ',' + str(row.age) + ',' + '"' + str(row.address) + '"' + ',' + str(row.gender) + ");"
        cursor.execute(query1)
    conn.commit()

if __name__ == "__main__":
    i=-1
    x=0
    for j in l:
        cursor.execute("CREATE TABLE student(id INT PRIMARY KEY, name VARCHAR(255), age INT, address VARCHAR(255), gender CHAR);")
        query = " create table studentc3 as select * from student where 1=2; "
        cursor.execute(query)
        start = time.time()
        t1 = threading.Thread(target=extract, args=(x,j))
        t1.start()
       end = time.time()
        diff1=end-start
        i = i+1
        df.loc[i, 2] = diff1
        cursor.execute("drop table student;")
        cursor.execute("drop table studentc3")
    df.to_csv('analysis.csv', index=False)

