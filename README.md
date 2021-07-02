# Multithreading-based-ETL-process

In this project, I have created a table in MySQL, extracted the data from it, Tranformed it and then Loaded it again in the table. This ETL process has been implemented in 3 cases (discussed below) and I have analyzed the amount of time it takes to run the 3 cases.
The above process has been done for different number of rows in the table i.e. 5000 rows, 10,000 rows, 15,0000 rows, 20,000 rows and 25,000 rows.

Database name: mydb

Table Column names: id, name, age, address, gender

Transformations applied on all records: <br>
1) Converted name to uppercase<br>
2) Added 1 to original age<br>
3) Converted address to uppercase<br>
4) Complemented the gender

CASE 1:<br>
1) Extracted data from table 'student1' <br>
2) Tranformed the data while Loading it to table 'studentc1'

CASE 2:<br>
1) Extracted data from table 'student2' to a file 'output.csv' <br>
2) Applied the transformations on the file.<br>
3) Loaded the data from the file to the table 'studentc2'

CASE 3:<br>
1) Extracted data from table 'student3' into a number of small files (each file contains a subset of the whole data)<br>
2) Applied the transformations on all the files simultaneously using <b>multithreading</b> (I have taken 5 threads here)<br>
3) Loaded the data from the files to the table 'studentc3'<br>
For the process of Multithreading, I have used the ThreadPoolExecutor class available in python. 

For all the above 3 cases and all the number of records, I have noted the time in 'analysis.csv' file.<br>
