from bs4 import BeautifulSoup
import csv
import time
import requests
import pandas as pd
start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
time.sleep(1)
page = requests.get(start_url, verify=False)
soup = BeautifulSoup(page.text,"html.parser")
starTable = soup.find("table")
tableRows = starTable.find_all("tr")
temp_list = []
for trtags in tableRows:
    tdTags = trtags .find_all("td")
    row = [i.text.rstrip() for i in tdTags]
    temp_list.append(row)
starNames = []
starDist= []
starMass = []
starRadius = []
starLum = []

for i in range(1,len(temp_list)):
    starNames.append(temp_list[i][1])
    starDist.append(temp_list[i][3])
    starMass.append(temp_list[i][5])
    starRadius.append(temp_list[i][6])
    starLum.append(temp_list[i][7])
df2 = pd.DataFrame(list(zip(starNames,starDist,starMass,starRadius,starLum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

df2.to_csv("stars.csv")

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(start_url, verify=False)
soup = BeautifulSoup(page.text,"html.parser")
tables = soup.find_all("table")
tableRows = tables[3].find_all("tr")
temp_list = []
for trtags in tableRows:
    tdTags = trtags.find_all("td")
    row = [i.text.rstrip() for i in tdTags]
    temp_list.append(row)
starNames = []
starDist= []
starMass = []
starRadius = []
starLum = []

for i in range(1,len(temp_list)):
    starNames.append(temp_list[i][0])
    starDist.append(temp_list[i][5])
    starMass.append(temp_list[i][8])
    starRadius.append(temp_list[i][9])
df2 = pd.DataFrame(list(zip(starNames,starDist,starMass,starRadius)),columns=['Star_name','Distance','Mass','Radius'])

df2.to_csv("dwarfStars.csv")
