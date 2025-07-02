***Dimensional modelling***

***it is of two types - 1) Dimension 2)Facts***



***1) Dimension  =*** *Data which can not be changed(eg. name , DOB ,Fathers name , Mothers name) or takes times to change(Address, Age)*



***SCD --> slowly changing dimension***

*types of SCD - 1)SCD type1      **2)**SCD type2<b>      3)</b>SCD type3*

***1)SCD type1  -***  <i>it is used when we want to get latest information and do not want historical data</i>

***2)SCD type2 -*** <i>it is used when we want to know which database is currently working, it is the most common SCD , it contains historical data</i>

***3)SCD type3-***  <i>it is of no use</i>





***2) Facts  =*** <i>it is a table where we store numeric value or metric data
</i>

* *OLTP (online Transaction Processing**) -** raw data, real time transaction*
* *OLAP (Online Analytical Processing**) -** analytical system*
* ***Data pipelines -***<i> converts OLTP data to OLAP </i>



***Dimensional modelling -*** 

* ***Star schema (***<i> better **)**</i>
* ***Snowflake Schema***
