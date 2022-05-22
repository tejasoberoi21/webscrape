from bs4 import BeautifulSoup
import csv
import time
import requests
start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
time.sleep(1)

headers = ["name","distance", "mass", "radius"]
starData = []
def webScrape():
    page = requests.get(start_url, verify=False)
    soup = BeautifulSoup(page.content,"html.parser")
    temp_list = []
    for trtags in soup.find_all("tr"):
        tdTags = trtags.find_all("td")
        for index,tdtag in enumerate(tdTags):
            try:
                if(index == 0):
                    temp_list.append(tdtag.find_all("a")[0].contents[0])
                else:
                    temp_list.append(tdtag.contents[0])
            except:
                temp_list.append("")
        starData.append(temp_list)
webScrape()
with open("stars.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(starData)

