# Multithreading-based-ETL-process

In this project, I have done a comparison of different techniques for tranforming a large dataset and compared the time taken in each technique.

For this, I have created a table in MySQL, extracted the data from it, Tranformed it and then Loaded it again in the table. This ETL process has been implemented in 3 cases (discussed below) and I have analyzed the amount of time it takes to run the 3 cases.
The above process has been done for different number of rows in the table i.e. 5000 rows, 10,000 rows, 15,0000 rows, 20,000 rows and 25,000 rows.

Database name: mydb

Table Column names: id, name, age, address, gender

Transformations applied on all records: <br>
1) Converted name to uppercase<br>
2) Added 1 to original age<br>
3) Converted address to uppercase<br>
4) Complemented the gender

CASE 0:<br>
1) Extracted data from table 'student1' <br>
2) Tranformed the data while Loading it to table 'studentc1'

CASE 1:<br>
1) Extracted data from table 'student2' to a file 'output.csv' <br>
2) Applied the transformations on the file.<br>
3) Loaded the data from the file to the table 'studentc2'

CASE 2:<br>
1) Extracted data from table 'student3' into a number of small files (each file contains a subset of the whole data)<br>
2) Applied the transformations on all the files simultaneously using <b>multithreading</b> (I have taken 5 threads here)<br>
3) Loaded the data from the files to the table 'studentc3'<br>
For the process of Multithreading, I have used the ThreadPoolExecutor class available in python. 

For all the above 3 cases and all the number of records, I have noted the time in 'analysis.csv' file.<br>
Result in analysis.csv:<br>

In the above table, the columns depict the 3 cases (case 0,1,2) taken and the rows show the different number of records taken (5000 rows, 10,000 rows, 15,0000 rows, 20,000 rows and 25,000 rows.)

<table>
  <tr>
    <td> CASE 0</td>
    <td> CASE 1</td>
    <td> CASE 2</td>
  </tr>
  <tr>
    <td>5000</td>
    <td>1.890067577</td>
    <td>5.041134357</td>
    <td>0.242992401</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>8.837369204</td>
    <td>10.03750229</td>
    <td>0.488361597</td>
  </tr>
  <tr>
    <td>15000</td>
    <td>1.531428337</td>
    <td>4.055989265</td>
    <td>1.608299494</td>
  </tr>
  <tr>
    <td>20000</td>
    <td>3.995323658</td>
    <td>7.610261917</td>
    <td>1.230496168</td>
  </tr>
  <tr>
    <td>25000</td>
    <td>1.074378967</td>	
    <td>7.832616568</td>	
    <td>0.915403366</td>
</table>


From the table, we can conclude that CASE2 i.e. the case in which I have done Multithreading takes the least time to complete.
