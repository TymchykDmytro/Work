from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
from pathlib import Path
home = Path.home()
wave_absolute = Path(home,"Desktop","Work-main","work","test3" ,"chromedriver.exe")
driver = webdriver.Chrome(wave_absolute)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
time.sleep(5)

driver.find_element(By.XPATH , ("/html/body/div[4]/div[3]/div/div/div/div[6]/div[1]/div/div/div/div[5]/pre[7]/span/span[7]")).click()
act=ActionChains(driver)
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

def test_equal1():
    act2= driver.find_element(By.TAG_NAME , ("cite"))
    assert act2.text == 'https://bing.com/travelguide?q=Redmond' or 'https://www.bing.com/travel/place-information' , "YOUR search is false"
time.sleep(5)
