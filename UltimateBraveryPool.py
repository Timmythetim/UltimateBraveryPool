from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

totalStuff = {}
driver = webdriver.Chrome()
flag = 0
totalStuff["Sums"] = []
totalStuff["Items"] = []
totalStuff["PrimaryRunes"] = []
totalStuff["SecondaryRunes"] = []
totalStuff["RuneStats"] = []
totalStuff["Champs"] = []
totalStuff["Ability"] = []

driver.get("https://www.ultimate-bravery.net/")
with open("output", "w") as f:
    for x in range(0, 5):
        time.sleep(.1)
        button = driver.find_element(By.ID, "braveryBtn")
        button.click()
        time.sleep(.5)
        champ = driver.find_element(By.CLASS_NAME, "champion-name").text
        for _ in totalStuff.values():
            if champ in _:
                flag = 1
        if flag == 0:
            ability = driver.find_element(By.CLASS_NAME, "up-fist-spell-to-maximize-img").text
            sums = driver.find_elements(By.XPATH, "//div[@class='ub-summoner-spells']/img")
            items = driver.find_elements(By.CLASS_NAME, "ub-item")
            # starterItem = driver.find_element(By.CLASS_NAME, "ub-role-item").find_element(By.XPATH, "//div[@class='ub-item']/img")
            runes = driver.find_element(By.CLASS_NAME, "ub-runes")
            primaryRunes = runes.find_element(By.CLASS_NAME, "ub-runes-primary").find_elements(By.TAG_NAME, "li")
            secondaryRunes = runes.find_element(By.CLASS_NAME, "ub-runes-secondary").find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")
            runeStats = driver.find_element(By.CLASS_NAME, "ub-rune-stats").find_elements(By.TAG_NAME, "div")
            totalStuff["Champs"].append(champ)
            totalStuff["Ability"].append(ability)
            
            for e in sums:
                totalStuff["Sums"].append(e.get_attribute("alt"))
            for i in range(0, len(items)):
                item = (i + 1, items[i].get_attribute("title"))
                totalStuff["Items"].append(item)
            for l in primaryRunes:
                totalStuff["PrimaryRunes"].append(l.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div").get_attribute("title"))
            for y in secondaryRunes:
                totalStuff["SecondaryRunes"].append(y.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div").get_attribute("title"))
            for z in runeStats:
                totalStuff["RuneStats"].append(z.get_attribute("title"))
        else:
            x -= 1
            flag = 0


    f.write(json.dumps(totalStuff, indent=2))