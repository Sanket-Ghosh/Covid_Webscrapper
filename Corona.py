from plyer import notification

import requests

import time

from bs4 import BeautifulSoup

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C://Users//Sanket//Desktop//COVID Tracker//icon2.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':

        myHtmlData = getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())

        myDatastr = ''

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDatastr += tr.get_text()
        myDatastr = myDatastr[1:]
        itemList = myDatastr.split('\n\n')


        states = ['West Bengal','Delhi']

        for item in itemList[0:32]:
            dataList = item.split('\n')

            if dataList[1] in states:
                print(dataList)

                nTitle = "COVID-19 Cases"
                nText = f"State {dataList[1]}\nAffected: {dataList[2]}\nCured: {dataList[3]}\nDeath: {dataList[4]}"
                notifyme(nTitle,nText)

                time.sleep(5)


