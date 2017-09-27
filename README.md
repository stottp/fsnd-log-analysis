# Log Analysis Project

## About
This project on Udacity's FSND requires you to connect to a postgres database and use SQL to better understand users interaction on a website from analysing the web servers log files.

## Requirements
* Python 2.x
* Virtual Box
* Vagrant
* newsdata.sql

## What to install
* Install Vagrant and Virtual Box
* Clone or copy this repository to run
* [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) a copy of newsdata.sql

## How to run
1. cd to vagrant directory
2. run _vagrant up_ to run vagrant on vm
3. run _vagrant ssh_ to login into vm
4. use the command _psql -d news -f newsdata.sql_. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
5. run _log_analyis.py_
