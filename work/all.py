import requests
import pytest
import base64
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from pathlib import Path

img = requests.get("http://apimeme.com/meme?meme=Alarm-Clock&top=Top+text&bottom=Bottom+text")
with open("example.jpeg", 'wb') as file:
    file.write(img.content)
with open("example.jpeg", 'rb') as f:
    base64dec = base64.b64decode(f.read())
    base64 = base64.b64encode(base64dec)

def test_equal1():
    assert base64[0] == 74 , 'It must be J'
    assert base64[1] == 70 , 'It must be F'
    assert base64[2] == 73 , 'It must be I'
    assert base64[3] == 70 , 'It must be F'

ask = img.headers['Content-Type']
def test_equal():
    assert ask == 'image/jpeg'
base=sqlite3.connect('data.db')
curs=base.cursor()
pop=curs.execute("""SELECT population FROM Countries WHERE id == 'USA'""").fetchone()
ar=curs.execute("""SELECT area FROM Countries WHERE id == 'USA' """).fetchone()
base.commit()
print("Популяція : " + str(pop[0]))
print("Площа : " + str(ar[0]))
density= int(pop[0])/int(ar[0])
print("Плотность: " + str(density))
def test_equal2():
    assert density < 50, f"Density is lower than 50"
ind = curs.execute("""SELECT population FROM Countries""").fetchall()
sum=0
for x in ind:
    sum+=int(x[0])
print("Сума:" + str(sum))
def test_equal3():
    assert sum < 2000000000, f"Sum must be lower than 2000000000"
home = Path.home()
wave_absolute = Path(home,"Desktop","Work-main","work","test3" ,"chromedriver.exe")
driver = webdriver.Chrome(wave_absolute)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
time.sleep(5)

driver.find_element(By.XPATH , ("/html/body/div[4]/div[3]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre[7]/span/span[7]")).click()
act=ActionChains(driver)
#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.key_down(Keys.BACK_SPACE).key_up(Keys.BACK_SPACE).perform()
act.send_keys('"https://www.bing.com"').perform()
act.send_keys('id="iframe"').perform()
time.sleep(5)
element = driver.find_element(By.ID , ("runbtn")).click()
driver.switch_to.frame("iframeResult")
driver.switch_to.frame("iframe")
time.sleep(5)
driver.find_element(By.XPATH , ("/html/body/div[2]/div/div[3]/div[2]/form/input[1]")).send_keys('redmond')
time.sleep(5)
act1 = driver.find_element(By.ID , ("sa_5003")).click()
time.sleep(5)
act2= driver.find_element(By.TAG_NAME , ("cite"))

def test_equal4():
    act2= driver.find_element(By.TAG_NAME , ("cite"))
    assert act2.text == 'https://bing.com/travelguide?q=Redmond' or 'https://www.bing.com/travel/place-information' , "YOUR search is false"
time.sleep(5)
