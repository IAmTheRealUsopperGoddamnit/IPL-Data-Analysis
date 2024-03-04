# IPL-Data-Analysis
Data Analysis of IPL Matches from 2008-2020.
You can choose to see general analytics presented in graphs, filter, and sort data to your liking.
There are two versions of this code—Python & MySQL integrated version, and Python version.

In the Python & MySQL integrated verison, you cannot filter or sort data, but you instead enjoy a backend functionality which provides you additional information under graphs. Additionally, make sure to put your matchpython.csv and matchsql.csv files in "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads" to bypass the error, "The MySQL server is running with the --secure-file-priv option so it cannot execute this statement". If you still have this error, go to MySQL 8.0 Command Line Client and type "SHOW VARIABLES LIKE "secure_file_priv";". This will show you the path where you can add the csv files to bypass the above error.

Keep in mind inputting is case-sensitive, so make sure to provide identical capitalization as shown in the options.
Enjoy.
