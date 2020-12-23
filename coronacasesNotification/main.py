from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='icon.ico',
        timeout=15
    )


def getDatafromUrl(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    notifyMe("Pranav", "Lets fight the spread of this virus together")
    myhtmldata = getDatafromUrl('https://www.mohfw.gov.in/')
    # print(myhtmldata)
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    # print(soup.prettify())
    mydatastr = ""
    for tr in soup.find_all('table')[0].find_all('tr'):
        mydatastr = mydatastr + tr.get_text()

    mydatastr = mydatastr[1:]
    itemlist = mydatastr.split('\n\n')
    itemlist = itemlist[:len(itemlist)-2]
    print(itemlist)
    state = ('Chandigarh', 'Rajasthan', 'Uttar Pradesh')
    for item in itemlist[:34]:
        datalist = item.split('\n')
        # print(item)
        # print(datalist)
        if datalist[1] in state:
            # print(datalist)
            nTitle = 'cases of covid-19'
            nText = f"{datalist[1]}:Ind :{datalist[2]}"
            notifyMe(nTitle, nText)
            time.sleep(2)
