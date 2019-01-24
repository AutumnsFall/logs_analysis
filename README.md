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

## Setup

Make sure you have the packages required to run. If you don't please install.

`sudo apt install python3 python3-pip`
`sudo apt install make zip unzip postgresql`
`sudo apt install flask psycopg2-binary`

## How to use

####To run the server, 

> python3 server.py

And go to 0.0.0.0:8000/

Enjoy
