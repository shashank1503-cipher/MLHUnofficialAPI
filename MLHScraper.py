import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import AddToDB
def getDetails(html,year):
    hackDic = {}
    soup = BeautifulSoup(html, "html.parser")
    eventLink = soup.a['href']
    hackDic['eventLink']= eventLink.strip()
    heroImageSrc = soup.find(class_="image-wrap").img['src']
    hackDic['heroImageSrc']= heroImageSrc.strip()
    logoImageSrc = soup.find(class_="event-logo").img['src']
    hackDic['logoImageSrc']= logoImageSrc.strip()
    eventName = soup.find(class_="event-name").text
    hackDic['eventName']= eventName.strip()
    eventDate = soup.find(class_="event-date").text
    hackDic['eventDate']= eventDate.strip()
    eventLocation = soup.find(class_="event-location").text
    eventLocation = ''.join(eventLocation.split())
    hackDic['eventLocation']= eventLocation
    eventNotes = soup.find(class_="event-hybrid-notes").text
    hackDic['eventNotes']= eventNotes.strip()
    hackDic['year'] = year
    return hackDic
def db(hackathons):
    for i in hackathons:
        if (AddToDB.fetchCountFromDb({'eventLink' : i['eventLink']})) == 1:
            AddToDB.addToDB(i)

        
if __name__ == "__main__":
    URL = "https://mlh.io/seasons/2021/events"
    driver = webdriver.Chrome('C:/bin/chromedriver') 
    driver.get(URL)

    time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all(class_ = "event-link")
    hackathons = []
    hackathonDetails = []
    for result in results:
        hackathons.append(result.prettify())
    for i in hackathons:
        hackathonDetails.append(getDetails(i,'2021'))
    print(hackathonDetails)
    db(hackathonDetails)  
