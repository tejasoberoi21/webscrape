from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import requests
start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/tejasoberoi/Downloads/chromedriver")
browser.get(start_url)
time.sleep(1)

headers = ["name","light years from earth", "planet mass", "stellar magnitude", "discovery date", "hyperlinks", "planet_type", "planet_mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planetData = []
def webScrape():
    for i in range(202):
        bs = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in bs.find_all("ul",attrs = {"class","exoplanet"}):
            litags = ultag.find_all("li")
            temp_list = []
            for index,li in enumerate(litags):
                if(index == 0):
                    temp_list.append(li.find_all("a")[0].contents[0])

                else:
                    try:
                        temp_list.append(li.contents[0])
                    except:
                        temp_list.append("")
            planetData.append(temp_list)
            hyperlink_li_tag = litags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href=True)[0]["href"])
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
planetData2 = []
def moreScraping(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.parser")

    temp_list = []
    for trtags in soup.find_all("tr",attrs = {"class","fact_row"}):
        tdTags = trtags.find_all("td")
        for tdtag in tdTags:
            try:
                temp_list.append(tdtag.find_all("div",attrs={"class","value"})[0].contents[0])
            except:
                temp_list.append("")
    planetData2.append(temp_list)
    moreScraping(hyperlink)
webScrape()
for index,data in enumerate(planetData):
    moreScraping(data[5])
finalData = []
for index,data in enumerate(planetData):
    newData = planetData2[index]
    newData = [element.replace("\n","") for element in newData]
    print(newData)
    newData = newData[:7]
    finalData.append(data+newData)
with open("planets.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(finalData)

