import mysql.connector
import random
import pandas as pd
import csv
import pymysql
import threading
import time
from concurrent.futures import ThreadPoolExecutor

#case 3

l=[5,10,15,20,25]

df=pd.read_csv("analysis.csv")
conn = pymysql.connect(host="localhost", user='root', password='alaskayoung', database='MYDB')
cursor = conn.cursor()

def extract(x,j):
    conn = pymysql.connect(host="localhost", user='root', password='alaskayoung', database='MYDB')
   # print("started j", j)
    print("started x", x)
    query = 'select * from student limit ' + str(int(x)) + ', ' + str(int(j-x)) + ';'
    print(query)
    results = pd.read_sql_query(query, conn)
    results.to_csv("output" + str(int(x)) + ".csv", index=False)
    transform("output" + str(int(x)) + ".csv")
    #print("end j", j)

def transform(file):
     data = pd.read_csv(file)
     print(data)
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
        cursor = conn.cursor()
        cursor.execute(query1)
     conn.commit()

if __name__ == "__main__":
    i=-1
    x=0
    for j in l:
        print(j)
        conn = pymysql.connect(host="localhost", user='root', password='alaskayoung', database='MYDB')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE student (id INT PRIMARY KEY, name VARCHAR(255), age INT, address VARCHAR(255), gender CHAR);")
        for ix in range(0, j):
             query = "insert into student values(" + str(ix) + ',' + " 'name" + str(ix) + "'," + str(
                  random.randint(3, 100)) + ',' + ' "Delhi" ' + ',' + ' 0 ' ");"
             cursor.execute(query)
        conn.commit()
        query = " create table studentc3 as select * from student where 1=2; "
        cursor.execute(query)
        start = time.time()
        value1=[x,x+(j/5),x+2*(j/5),x+3*(j/5),x+4*(j/5)]
        value2=[j/5,2*(j/5),3*(j/5),4*(j/5),5*(j/5)]
        with ThreadPoolExecutor(5) as exe:
            #exe.submit(extract,x, j/5)
            exe.map(extract, value1,value2)
        end = time.time()
        diff1=end-start
        i = i+1
        df.loc[i, 2] = diff1
        conn.ping(reconnect=True)
        cursor.execute("drop table student;")
        cursor.execute("drop table studentc3")
    df.to_csv('analysis.csv', index=False)

