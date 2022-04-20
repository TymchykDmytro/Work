import sqlite3
import requests
import pytest
base=sqlite3.connect('data.db')
curs=base.cursor()
pop=curs.execute("""SELECT population FROM Countries WHERE id == 'USA'""").fetchone()
ar=curs.execute("""SELECT area FROM Countries WHERE id == 'USA' """).fetchone()
base.commit()
print("Популяція : " + str(pop[0]))
print("Площа : " + str(ar[0]))
density= int(pop[0])/int(ar[0])
print("Плотность: " + str(density))
def test_equal():
    assert density < 50, f"Density is lower than 50"
ind = curs.execute("""SELECT population FROM Countries""").fetchall()
sum=0
for x in ind:
    sum+=int(x[0])
print("Сума:" + str(sum))
def test_equal1():
    assert sum < 2000000000, f"Sum must be lower than 2000000000"
