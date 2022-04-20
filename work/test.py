import sqlite3
import requests
import pytest
base=sqlite3.connect('data.db')
curs=base.cursor()
base.execute("""CREATE TABLE IF NOT EXISTS Countries (id TEXT PRIMARY KEY, population INTEGER ,area INTEGER)""")
curs.execute("""INSERT INTO Countries VALUES(?,?,?)""", ( 'Ukraine','41588354','603628'))
curs.execute("""INSERT INTO Countries VALUES(?,?,?)""", ( 'France','67399000','640679'))
curs.execute("""INSERT INTO Countries VALUES(?,?,?)""", ('USA','328239523','9833520'))
curs.execute("""INSERT INTO Countries VALUES(?,?,?)""", ( 'China','1400050000','9596961'))
base.commit()
