# This repository is for Logs analysis project

## Contents

- config.py
- index.py
- logsdb.py
- README.md
- server.py

## Brief Explanations what each file does

#### config.py

Your database name should be put in here. If you want to change your database name, you should change it from this file.

#### index.py

This is the HTML template the server will use for response. Have a look around.

#### logsdb.py

This is where the database queries and connections are happening.

If you want to reuse the modules, import this file and call the modules.

#### README.md

You are reading it right now.

#### server.py

This is where the server code resides. It uses flask.

## Program Setup

Make sure you have the packages required to run. If you don't please install.

`sudo apt install python3 python3-pip`

`sudo apt install flask psycopg2-binary`

## Database Setup

This application uses Postgresql, a type of SQL database. You will need to install this on your machine.

To install the database :

`sudo apt install make zip unzip postgresql`

#### Database setup

You will need to set up your database. To run this app, prior assumptions will be that you have a database name called "news".

For setting up the Postgresql step by step and user friendly instructions, refer to https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

You can create new database in the psql console with 

`create database news;` 

After creating the database "news", there should be three tables in that database. You can create tables by 

`create table name (
	columnName datatype, 
	...
)`

#### Required Tables

- articles (author integer, title text, lead text, body text, time timestamp, id integer)
- authors (name text, bio text, id integer)
- log (path text, ip inet, method text, status text, time timestamp, id integer)

###### "articles" Table

This is where the articles written by the authors will be stored. 

Columns are:
author : contains author id
title : title of the article
lead : lead text
body : body of the article
time : the time the article was published
id : unique key for each article (article id)

###### "authors" Table

This is where the authors will be stored.

Columns are:
name : name of the author
bio : biography of the author
id : unique key for each author (author id)

###### "log" Table

This is where the logs of the server that keeps track of requests made by users.

Columns are:
path : the url that the users request to server
method : the method the users use (Like GET, POST, PUT, DELETE)
status : response code by server. (200 ok, 404 NOT FOUND)
time : the time the request was made
id : unique key for each log (log id)

#### Importing Data

If you have exported data, you can easily import it from terminal.

Go to the directory the exported file is located, assume the file is "backup.sql"

`psql news < backup.sql`

And the data will be imported.

#### Exporting Data

You can export the data with

`psql news > backup.sql`

## How to use

You can either run with the server or reuse the functions provided.

#### To run the server, 

> python3 server.py

And go to 0.0.0.0:8000/


Enjoy
