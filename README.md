# Multithreading-based-ETL-process

In this project, I have created a table in MySQL, extracted the data from it, Tranformed it and then Loaded it again in the table. This ETL process has been implemented in 3 cases and I have analyzed the amount of time it takes to run the 3 cases.
The above process has been done for different number of rows in the table i.e. 5000 rows, 10,000 rows, 15,0000 rows, 20,000 rows and 25,000 rows.

Database name: mydb<br>
Table Column names: id, name, age, address, gender<BR>
Transformations applied on all records: <br>
1) converted name to uppercase<br>
2) added 1 to original age<br>
3) converted address to uppercase<br>
4) complemented the gender

CASE 1:
Extracted data from table 'student1' <br>
Tranformed the data while Loading it to table 'studentc1'

CASE 2:
